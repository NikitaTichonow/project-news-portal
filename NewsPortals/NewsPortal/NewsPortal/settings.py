import os
from pathlib import Path
from django.conf import settings
from django.core.mail import mail_admins
import logging

logger = logging.getLogger("django")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# ВНИМАНИЕ ПО БЕЗОПАСНОСТИ: держите секретный ключ, используемый в производстве, в секрете!
SECRET_KEY = 'django-insecure-c($xn2pney1r-4s-3+wh6jh7$&*x_-m_&m61_gukp6&kynkyi0'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = []


# DEBUG = False

# ALLOWED_HOSTS = ['http://127.0.0.1:8000']


LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

# DEBUG = False
#
# ALLOWED_HOSTS = ["http://127.0.0.1:8000/"]

INSTALLED_APPS = [
    'modeltranslation',
    # приложение, которое позволяет делать удобные переводы в моделях. (pip install django-modeltranslation)

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'news',
    'accounts',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # AccountMiddleware действует как связующее звено между
    # процессом обработки запросов Django, системой сессий, аутентификацией и перенаправлениями,
    # это ключевой элемент для работы 'django-allauth'.
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'NewsPortal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                # для `allauth` обязательно нужен этот процессор ('django.template.context_processors.request',)
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'NewsPortal.wsgi.application'

LANGUAGES = [
    ('en-us', 'English'),
    ('ru', 'Русский')
]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': '09011996',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     },
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "/"

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# 'none' - проверка email — отсутствует;
# 'mandatory' — не пускать пользователя на сайт до момента подтверждения почты;
# 'optional' — сообщение о подтверждении почты будет отправлено, но пользователь может залогиниться на сайте
# без подтверждения почты.


ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

# Блок кода настроек нашего проекта работы с почтой (Yandex-почтой)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# класс отправителя сообщений (у нас установлено значение по умолчанию, а значит, эта строчка не обязательна)
EMAIL_HOST = 'smtp.yandex.ru'
# Хост почтового сервера - это адрес или доменное имя сервера, который обрабатывает и отправляет электронную почту.
# Хост почтового сервера может быть использован как для отправки, так и для получения почты
EMAIL_PORT = 465
"""
Порт, на который почтовый сервер принимает письма, называется почтовым портом. 
Один из самых распространенных почтовых портов - это порт 25, который используется для передачи электронной почты 
по протоколу SMTP (Simple Mail Transfer Protocol). 
Однако, существуют и другие почтовые порты, 
такие как порт 587, который используется для SMTP с шифрованием TLS (Transport Layer Security), 
и порт 465, который используется для SMTP с шифрованием SSL (Secure Sockets Layer). 
Использование конкретного почтового порта зависит от настроек и требований почтового сервера.
"""
EMAIL_HOST_USER = "nik7674"
# логин пользователя почтового сервера
EMAIL_HOST_PASSWORD = "ycfaqosthahpjawi"
# пароль пользователя почтового сервера
EMAIL_USE_TLS = False
# необходимость использования TLS
# (зависит от почтового сервера, смотрите документацию по настройке работы с сервером по SMTP)
EMAIL_USE_SSL = True
# необходимость использования SSL
# (зависит от почтового сервера, смотрите документацию по настройке работы с сервером по SMTP)


DEFAULT_FROM_EMAIL = "nik7674@yandex.ru"
# почтовый адрес отправителя по умолчанию
# Последняя строчка будет использоваться как значение по умолчанию для поля from в письме.
# То есть будет отображаться в поле «отправитель» у получателя письма

SERVER_EMAIL = "nik7674@yandex.ru"
# SERVER_EMAIL содержит адрес почты, от имени которой будет отправляться письмо при вызове mail_admins и mail_manager.
# А переменная MANAGERS будет хранить список имён менеджеров и адресов их почтовых ящиков.

ADMINS = (
    ('nik7674', 'nik7674@yandex.ru'),
)

EMAIL_SUBJECT_PREFIX = 'News Portal'

CELERY_BROKER_URL = 'redis://localhost:6379'  # указывает на URL брокера сообщений (Redis). По умолчанию он находится на порту 6379.
CELERY_RESULT_BACKEND = 'redis://localhost:6379'  # указывает на хранилище результатов выполнения задач.
CELERY_ACCEPT_CONTENT = ['application/json']  # допустимый формат данных.
CELERY_TASK_SERIALIZER = 'json'  # метод сериализации задач.
CELERY_RESULT_SERIALIZER = 'json'  # метод сериализации результатов.

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
        # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
        'TIMEOUT': 60
    }
}


# Определяем путь к логам
LOG_DIR = os.path.join(BASE_DIR, 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

# Настройка логирования
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '{levelname} {asctime} {message} {pathname} {exc_info}',
            'style': '{',
        },
        'general': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'errors': {
            'format': '{levelname} {asctime} {message} {pathname} {exc_info}',
            'style': '{',
        },
        'security': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'email': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'filters': {
        'debug_filter': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': lambda record: DEBUG,
        },
        'release_filter': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': lambda record: not DEBUG,
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
            'filters': ['debug_filter'],
        },
        'general_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'general.log'),
            'formatter': 'general',
            'filters': ['release_filter'],
        },
        'errors_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'errors.log'),
            'formatter': 'errors',
        },
        'security_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'security.log'),
            'formatter': 'security',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'email',
        },
    },
    'loggers': {
        # Основной логгер Django
        'django': {
            'handlers': ['console', 'general_file', 'errors_file', 'security_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        # Логгер для запросов
        'django.request': {
            'handlers': ['mail_admins', 'errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Логгер для сервера
        'django.server': {
            'handlers': ['mail_admins', 'errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Логгер для шаблонов
        'django.template': {
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Логгер для базы данных
        'django.db.backends': {
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Логгер для безопасности
        'django.security': {
            'handlers': ['security_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
