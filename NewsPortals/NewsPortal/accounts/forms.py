from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import send_mail, EmailMultiAlternatives, mail_admins


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)

        subject = 'Добро пожаловать !'
        text = f'{user.username}, вы успешно зарегистрировались на сайте!'
        html = (
            f'<b>{user.username}</b>, вы успешно зарегистрировались на '
            f'<a href="http://127.0.0.1:8000">сайте</a>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

        mail_admins(
            subject='Новый пользователь!',
            message=f'Пользователь {user.username} зарегистрировался на сайте.'
        )

        return user