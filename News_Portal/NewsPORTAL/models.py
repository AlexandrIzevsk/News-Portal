from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg, Min, Max, Sum  # noqa
from django.db.models.functions import Coalesce
from django.core.cache import cache
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='users', verbose_name=pgettext_lazy('help text for Author model', 'This is the help text'))
    rating = models.IntegerField(default=0)

    def update_rating(self):
        posts_rating = self.post_set.aggregate(
            pr=Coalesce(Sum('rating'), 0)
        ).get('pr')
        comments_rating = self.user.comment_set.aggregate(
            cr=Coalesce(Sum('rating'), 0)
        ).get('cr')
        posts_comments_rating = self.post_set.aggregate(
            pcr=Coalesce(Sum('comment__rating'), 0)
        ).get('pcr')

        print(posts_rating)
        print('----------------')
        print(comments_rating)
        print('----------------')
        print(posts_comments_rating)

        self.rating = posts_rating * 3 + comments_rating + \
                      posts_comments_rating  # noqa
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True, help_text=_('category name'))

    def __str__(self):
        return self.name


class Post(models.Model):
    paper = 'PA'
    news = 'NS'

    CHOICES = [
        (paper, 'Статья'),
        (news, 'Новость')
    ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
        verbose_name=pgettext_lazy('help text for Post model', 'Author'))
    categorys = models.ManyToManyField(Category, through='PostCategory',
        verbose_name=pgettext_lazy('help text for Post model', 'Category'))
    choice = models.CharField(max_length=2, choices=CHOICES, default=news)
    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128, verbose_name=pgettext_lazy('help text for Post model', 'Title'))
    text = models.TextField(verbose_name=pgettext_lazy('Help', 'Text'))
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} - {self.preview()}'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'

    def get_absolute_url(self):
        if self.choice == 'NS':
            return reverse('news_detail', args=[str(self.id)])
            # return reverse('news-detail', args=[str(self.id)])

        elif self.choice == 'PA':
            return reverse('articles_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post - {self.pk}')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


# class Subscription(models.Model):
class Subscriber(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
