from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment


def nulfy_rating(modeladmin, request, queryset):
    queryset.update(rating=0)
    nulfy_rating.short_description = 'Обнулить товары'

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating')
    list_filter = ('rating',)
    search_fields = ('user__username',)
    actions = [nulfy_rating]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'choice', 'author', 'rating', 'time_in')
    list_filter = ('author__user__username', 'rating',)
    search_fields = ('author__user__username',)
    actions = [nulfy_rating]


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('post', 'category')
    list_filter = ('post__choice', 'post__author__user__username')
    search_fields = ('category__name','post__author__user__username')
    actions = [nulfy_rating]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Comment)
