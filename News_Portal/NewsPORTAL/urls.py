from django.urls import include, path
from django.views.generic import TemplateView
# Импортируем созданное нами представление
from .views import (
    NewsList, OneNewsDetail, News_SearchList, NewsCreate, NewsUpdate,
    NewsDelete, ArticlesCreate, ArticlesList, Articles_SearchList,
    ArticlesUpdate, ArticlesDelete, OneArticlesDetail,
    subscriptions
)
from NewsPORTAL import viewsets

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', viewsets.PostViewset)
router.register(r'news', viewsets.NewsViewset, basename='news')
router.register(r'articles', viewsets.ArticleViewset, basename='articles')
router.register(r'categories', viewsets.CategoryViewset)
router.register(r'post_category', viewsets.PostCategoryViewset)
router.register(r'authors', viewsets.AuthorViewset)
router.register(r'users', viewsets.UserViewset)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    )),
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
    path('subscriptions/', subscriptions, name='subscriptions'),
]
