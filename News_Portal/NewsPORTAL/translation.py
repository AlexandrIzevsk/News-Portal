from .models import Category, Post, Author
from modeltranslation.translator import register, TranslationOptions


# регистрируем наши модели для перевода

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)  # указываем, какие именно поля надо переводить в виде кортежа


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('author', 'categorys', 'title', 'text',)


@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('user__username',)
