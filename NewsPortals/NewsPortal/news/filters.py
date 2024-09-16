import django_filters
from django_filters import FilterSet

from .models import *  # (*) Импорт всех моделей
from django import forms

class PostFilter(django_filters.FilterSet):
    """
    Создаем свой набор фильтров для модели Post.
    FilterSet, который мы наследуем, должен чем-то напомнить знакомые вам Django дженерики.
    """
    # поиск по названию
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='Заголовок',
                                      widget=forms.TextInput(attrs={'placeholder': 'Поиск по названию'}))
    # # поиск по автору
    author = django_filters.ModelChoiceFilter(field_name='author', empty_label='Все авторы', label='Авторы',
                                              queryset=Author.objects.all())
    # поиск по типу
    categoryType = django_filters.ChoiceFilter(field_name='categoryType', empty_label='Все типы', label='Тип',
                                       choices=Post.CATEGORY_CHOICES)
    # поиск по категории
    postCategory = django_filters.ModelChoiceFilter(field_name='postCategory', empty_label='Все категории',
                                                    label='Категория', queryset=Category.objects.all())
    # поиск по дате
    dateCreation = django_filters.DateFilter(field_name='dateCreation', lookup_expr='gte', label='Дата',
                                             widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        """
        В Meta классе мы должны указать Django модель, в которой будем фильтровать записи.
        """
        model = Post
        # В fields мы описываем по каким полям модели будет производиться фильтрация.
        fields = ['categoryType', 'author', 'title', 'postCategory', 'dateCreation']


