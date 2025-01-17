from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'time_in',
            'title',
            'text',
            'rating',
            'author',
            'categorys',
        ]


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'time_in',
            'title',
            'text',
            'rating',
            'author',
            'category',
        ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.CharField(source="get_name_of_category_display")
    class Meta:
        model = Category
        fields = [
            'id',
            'category',
        ]


class PostCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostCategory
        fields = ['category']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'user',
            'rating',
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    time_in = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    rating = serializers.FloatField(read_only=True)
    categories = PostCategorySerializer(many=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'time_in',
            'choice',
            'title',
            'text',
            'rating',
            'author',
            'categories',
        ]

    def create(self, validated_data, **kwargs):
        categories = validated_data.pop('categories')
        post = Post.objects.create(**validated_data)

        for cat in categories:
            category = cat.pop("category")
            PostCategory.objects.create(category=category, post=post)

        return post
