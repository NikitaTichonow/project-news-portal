from django.urls import path, include
from . import views
from .views import NewsList, NewsDetail, Search, NewsCreate, NewsDelete, NewsEdit, ArticleList, ArticleDetail, ArticleDelete, ArticleEdit, subscriptions, Test_page
from django.views.decorators.cache import cache_page
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', cache_page(60 * 1)(views.start), name='home'),  # URL-шаблон Стартовой страницы
    path('news_list/', cache_page(60 * 5)(views.NewsList.as_view()), name='news_list'),  # URL-шаблон для списка новостей
    path('news_list/<int:pk>', views.NewsDetail.as_view(), name='news_detail'),  # URL-шаблон для списка новостей
    path('search/', views.Search.as_view(), name='search'),  # URL-шаблон Поисковой страницы
    path('news_create/', views.NewsCreate.as_view(), name='news_create'),  # URL-шаблон для создания новостей
    path('news_edit/<int:pk>', views.NewsEdit.as_view(), name='news_edit'),   # URL-шаблон для редактирования новостей
    path('news_delete/<int:pk>', views.NewsDelete.as_view(), name='news_delete'),  # URL-шаблон для удаления новостей
    path('article_list/', views.ArticleList.as_view(), name='article_list'),  # URL-шаблон для списка статей
    path('article_detail/<int:pk>', views.ArticleDetail.as_view(), name='article_detail'),  # URL-шаблон для списка статей
    path('article_create/', views.ArticleCreate.as_view(), name='article_create'),  # URL-шаблон для создания статей
    path('article_edit/<int:pk>', views.ArticleEdit.as_view(), name='article_edit'),   # URL-шаблон для редактирования статей
    path('article_delete/<int:pk>', views.ArticleDelete.as_view(), name='article_delete'),   # URL-шаблон для удаления статей
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('test/', views.Test_page.as_view()),
]



