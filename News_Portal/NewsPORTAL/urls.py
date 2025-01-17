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
    ))
]
