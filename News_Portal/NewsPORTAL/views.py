from django.contrib.auth.mixins import PermissionRequiredMixin #LoginRequiredMixin
from django.urls import reverse_lazy
from datetime import datetime
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import (
    Post, Category, Subscriber, #Subscription
)
from .filters import News_SearchFilter
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from .tasks import my_job
from django.http import HttpResponse
from django.views import View


class NewsList(ListView):
    queryset = Post.objects.filter(choice='NS').order_by('-time_in')
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Распродажа в среду!"


        return context


class News_SearchList(ListView):
    queryset = Post.objects.filter(choice='NS').order_by('-time_in')
    template_name = 'news_search.html'
    context_object_name = 'news'
    paginate_by = 2

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queruset = super().get_queryset()
        self.filterset = News_SearchFilter(self.request.GET, queruset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset

        return context


class OneNewsDetail(DetailView):
    # model = Post
    queryset = Post.objects.filter(choice='NS')
    template_name = 'one_news.html'
    context_object_name = 'post'


# Добавляем новое представление для создания новости.
class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('NewsPORTAL.add_post',)
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'news_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.choice = 'NS'
        return super().form_valid(form)


# Добавляем представление для изменения новости.
class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('NewsPORTAL.change_post',)
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'news_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.choice = 'NS'
        return super().form_valid(form)


# Представление удаляющее новость.
class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


class ArticlesList(ListView):
    queryset = Post.objects.filter(choice='PA').order_by('-time_in')
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 2


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Распродажа в среду!"

        return context


class OneArticlesDetail(DetailView):
    # model = Post
    queryset = Post.objects.filter(choice='PA')
    template_name = 'one_news.html'
    context_object_name = 'post'


class Articles_SearchList(ListView):
    queryset = Post.objects.filter(choice='PA').order_by('-time_in')
    template_name = 'articles_search.html'
    context_object_name = 'articles'
    paginate_by = 2

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queruset = super().get_queryset()
        self.filterset = News_SearchFilter(self.request.GET, queruset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset

        return context



class ArticlesCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('NewsPORTAL.add_post',)
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'articles_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.choice = 'PA'
        return super().form_valid(form)


class ArticlesUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('NewsPORTAL.change_post',)
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'articles_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.choice = 'PA'
        return super().form_valid(form)


class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('articles_list')


#
@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            # Subscription.objects.create(user=request.user, category=category)
            Subscriber.objects.create(user=request.user, category=category)

        elif action == 'unsubscribe':
            # Subscription.objects.filter(
            Subscriber.objects.filter(
                    user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            # Subscription.objects.filter(
            Subscriber.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('name')
    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )


class IndexView(View):
    def get(self, request):
        my_job.delay()
        return HttpResponse('Hello!')
