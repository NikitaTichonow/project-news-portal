from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import PostCategory, Subscription


SITE_URL = 'http://127.0.0.1:8000'

def send_notifications(preview, pk, head, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{SITE_URL}/news_list/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=head,
        body='',
        from_email="nik7674@yandex.ru",
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(instance, sender, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.postCategory.all()
        subscribers_emails = []

        for cat in categories:
            subscribers = Subscription.objects.filter(category=cat)
            for sub in subscribers:
                if sub.user.email:
                    subscribers_emails.append(sub.user.email)

        send_notifications(instance.preview(), instance.pk, instance.title, subscribers_emails)

