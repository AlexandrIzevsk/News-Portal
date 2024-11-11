from django.db.models.signals import m2m_changed
# from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail.message import EmailMultiAlternatives

from .models import Post, PostCategory



@receiver(m2m_changed, sender=PostCategory)
# @receiver(post_save, sender=Post)
# def news_created(instance, action="post_add", **kwargs):
def notify_subscribers(sender, instance, **kwargs):
    # if kwargs['action'] == 'post_add':
    #     pass
    #


    print('Опубликована новость', instance)
    if kwargs['action'] == 'post_add':
        # return

        emails = User.objects.filter(
            subscriptions__category__in=instance.categorys.all()
        ).values_list('email', flat=True)
        subject = f'Новый товар в категории {instance.categorys.all()}'

        text_content = (
            f'Заголовок: {instance.title}\n'
            f'Текст: {instance.text}\n\n'
            f'Ссылка на новость/статью: http://127.0.0.1:8000{instance.get_absolute_url()}'
        )
        html_content = (
            f'Заголовок: {instance.title}<br>'
            f'Текст: {instance.text}<br><br>'
            f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
            f'Ссылка на новость/статью</a>'
        )
        for email in emails:
            msg = EmailMultiAlternatives(subject, text_content, None, [email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()