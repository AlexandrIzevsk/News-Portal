from rest_framework import viewsets
from .serializers import *
from .models import *


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class NewsViewset(viewsets.ModelViewSet):
    queryset = Post.objects.filter(choice='NS')
    serializer_class = NewsSerializer


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Post.objects.filter(choice='RA')
    serializer_class = ArticleSerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostCategoryViewset(viewsets.ModelViewSet):
    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer

