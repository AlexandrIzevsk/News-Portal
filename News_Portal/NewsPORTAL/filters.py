from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
from django.forms import DateTimeInput
from .models import Post, Category, PostCategory


class News_SearchFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='postcategory__category__name',
        queryset=Category.objects.all(),
        label='Category',
        empty_label='Любая',
    )


    added_after = DateTimeFilter(
        field_name='time_in',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }