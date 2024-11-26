from celery import shared_task
import datetime
from NewsPORTAL.models import Post
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail.message import EmailMultiAlternatives


@shared_task
def my_job():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_in__gte=last_week)
    categories = set(posts.values_list('categorys__name', flat=True))
    subscribers = set(User.objects.filter(
            subscriptions__category__name__in=categories).values_list(
            'email', flat=True)
    )
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,

    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
