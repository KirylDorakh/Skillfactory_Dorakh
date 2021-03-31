from django.core.mail import mail_managers
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.signals import request_finished

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from .tasks import mailing

from .models import Post, Category

@receiver(post_save, sender=Post)
def notify_managers_appointment(sender, instance, created, **kwargs):
    if created:
        subject = f'New post: {instance.headline}'
    else:
        subject = f'New post: {instance.headline} {instance.content}'

    mail_managers(
        subject=subject,
        message=f'New post: {instance.headline}. Made:{instance.author}. Category: {instance.categories.all()}. Date:{instance.post_time.strftime("%d %m %Y")}',
    )
# post_save.connect(notify_managers_appointment, sender=Post)

@receiver(m2m_changed, sender=Post.categories.through)
def notify_subscribers(sender, action, instance, **kwargs):

    if action == 'post_add':

        new_post_categories = instance.categories.all()
        list_of_users_emails = []
        list_of_users_cat = []
        for cat in new_post_categories:
            list_of_users_cat.append(cat.name)
            subs = cat.subscribers.all()
            for sub in subs:
                list_of_users_emails.append(sub.email)
        cat = ' '.join(list_of_users_cat)

        pid = instance.id
        mailing.apply_async([pid], countdown = 5)

        link_id = instance.id
        link = f'http://127.0.0.1:8000/news/{link_id}'
        # получем наш html
        html_content = render_to_string('subscribers/mail_subscription_update.html',
                                        {
                                            'appointment': instance, 'link': link, 'categories': cat
                                        }
                                        )
        msg = EmailMultiAlternatives(
            subject=f'Новый пост from signals',
            body=f'{instance.headline}, {instance.preview()}, {instance.id}', #  это то же, что и message
            from_email='kir.dorakh@mail.ru',
            to=list_of_users_emails
        )
        msg.attach_alternative(html_content, "text/html") # добавляем html

        msg.send() # отсылаем

