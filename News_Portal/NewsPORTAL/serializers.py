from .models import *
from rest_framework import serializers


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = '__all__'


class PostSerializer(serializers.HyperlinkedModelSerializer):
    categorys = PostCategorySerializer(many=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'categorys']



class CategorySerializer(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'posts']
        extra_kwargs = {'posts': {'required': False}}



# class PostSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Post
#        fields = ['author', 'categorys', 'title', 'text', 'choice']

