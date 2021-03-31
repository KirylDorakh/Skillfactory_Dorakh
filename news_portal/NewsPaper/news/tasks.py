from celery import shared_task

from datetime import datetime
import time

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from .models import Post, Category


@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")

@shared_task
def printer(N):
    for i in range(N):
        time.sleep(1)
        print(i+1)

@shared_task
def mailing(pid):
    print(f'Mailing, post_id - {pid}, {type(pid)}')
    new_post = Post.objects.get(id = pid)
    print(f'new post was created - {new_post.headline}')

    new_post_categories = new_post.categories.all()
    list_of_users_emails = []
    list_of_users_cat = []
    for cat in new_post_categories:
        list_of_users_cat.append(cat.name)
        subs = cat.subscribers.all()
        for sub in subs:
            list_of_users_emails.append(sub.email)
    print(list_of_users_cat)
    cat = ' '.join(list_of_users_cat)

    link_id = new_post.id
    link = f'http://127.0.0.1:8000/news/{link_id}'
    # получем наш html
    html_content = render_to_string('subscribers/mail_subscription_update.html',
                                    {
                                        'appointment': new_post, 'link': link, 'categories': cat
                                    }
                                    )
    msg = EmailMultiAlternatives(
        subject=f'Новый пост form celery',
        body=f'{new_post.headline}, {new_post.preview()}, {new_post.id}',  # это то же, что и message
        from_email='kir.dorakh@mail.ru',
        to=list_of_users_emails
    )
    msg.attach_alternative(html_content, "text/html")  # добавляем html

    msg.send()  # отсылаем


@shared_task
def every_week_mailing(pid):
    print('every_week_mailing')

    for cat in Category.objects.all():
        current_week = datetime.today().strftime("%V")

        posts = Post.objects.all().filter(categories=cat, post_time__week=current_week)

        for sub in cat.subscribers.all():
            html_content = render_to_string(
                'subscribers/following_mail_week.html',
                {
                    'news': posts,
                    'user': sub,
                    'category': cat,
                }
            )
            # отправляем письмо
            msg = EmailMultiAlternatives(
                subject=f'{sub.username}',
                # имя клиента будет в теме для удобства
                body=None,  # сообщение с кратким описанием проблемы
                from_email='kir.dorakh@mail.ru',  # здесь указываете почту, с которой будете отправлять
                to=[sub.email]
            )
            msg.attach_alternative(html_content, "text/html")  # добавляем html

            msg.send()
