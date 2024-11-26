from django.urls import path
# Импортируем созданное нами представление
from .views import (
    NewsList, OneNewsDetail, News_SearchList, NewsCreate, NewsUpdate,
    NewsDelete, ArticlesCreate, ArticlesList, Articles_SearchList,
    ArticlesUpdate, ArticlesDelete, OneArticlesDetail,
    subscriptions, IndexView
)
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('news/search/', News_SearchList.as_view(),
         name='news_search_list'),
    path('news/', cache_page(60)(NewsList.as_view()),
         name='news_list'),
    path('news/<int:pk>', cache_page(60*5)(OneNewsDetail.as_view()),
         name='news_detail'),
    path('news/create/', NewsCreate.as_view(),
         name='news_create'),
    path('news/<int:pk>/edit', NewsUpdate.as_view(),
         name='news_update'),
    path('news/<int:pk>/delete', NewsDelete.as_view(),
         name='news_delete'),
    path('articles/search/', Articles_SearchList.as_view(),
         name='articles_search_list'),
    path('articles/', ArticlesList.as_view(),
         name='articles_list'),
    path('articles/<int:pk>', OneArticlesDetail.as_view(),
         name='articles_detail'),
    path('articles/create/', ArticlesCreate.as_view(),
         name='articles_create'),
    path('articles/<int:pk>/edit', ArticlesUpdate.as_view(),
         name='articles_update'),
    path('articles/<int:pk>/delete', ArticlesDelete.as_view(),
         name='articles_delete'),
    path('subscriptions/', subscriptions,
         name='subscriptions'),
    path('', IndexView.as_view()),
]
