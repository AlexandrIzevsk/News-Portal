from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import Author, Post, PostCategory, Category, Comment
from pprint import pprint


class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    # model = Post
    # Поле, которое будет использоваться для сортировки объектов
    # ordering = '-rating'
    queryset = Post.objects.filter(choice='NS').order_by('-time_in')
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = "Распродажа в среду!"
        # pprint(context)
        pprint(context)
        return context



class OneNewsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    # model = Post
    queryset = Post.objects.filter(choice='NS')
    # Используем другой шаблон — one_news.html
    template_name = 'one_news.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'

