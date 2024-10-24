from django.urls import path
# Импортируем созданное нами представление
from .views import (
    NewsList, OneNewsDetail, News_SearchList, NewsCreate, NewsUpdate, NewsDelete, ArticlesCreate,
ArticlesList, Articles_SearchList, ArticlesUpdate, ArticlesDelete, OneArticlesDetail
)


urlpatterns = [
    # path — означает путь.
    # В данном случае путь ко всем товарам у нас останется пустым,
    # чуть позже станет ясно почему.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('news/search/', News_SearchList.as_view(), name='news_search_list'),
    path('news/', NewsList.as_view(), name='news_list'),
    path('news/<int:pk>', OneNewsDetail.as_view(), name='news_detail'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit', NewsUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete', NewsDelete.as_view(), name='news_delete'),
    path('articles/search/', Articles_SearchList.as_view(), name='articles_search_list'),
    path('articles/', ArticlesList.as_view(), name='articles_list'),
    path('articles/<int:pk>', OneArticlesDetail.as_view(), name='articles_detail'),
    path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit', ArticlesUpdate.as_view(), name='articles_update'),
    path('articles/<int:pk>/delete', ArticlesDelete.as_view(), name='articles_delete'),
]