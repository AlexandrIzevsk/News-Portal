from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg, Min, Max, Sum
from django.db.models.functions import Coalesce



class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        # posts_rating = Post.objects.filter(author=self).aggregate(pr=Coalesce(Sum('rating'), 0))['pr']
        # comments_rating = Comment.objects.filter(user=self.user).aggregate(cr=Coalesce(Sum('rating'), 0))['cr']
        # posts_comments_rating = Comment.objects.filter(post__author=self).aggregate(pcr=Coalesce(Sum('rating'), 0))['pcr']

        posts_rating = self.post_set.aggregate(pr=Coalesce(Sum('rating'), 0)).get('pr')
        comments_rating = self.user.comment_set.aggregate(cr=Coalesce(Sum('rating'), 0)).get('cr')
        posts_comments_rating = self.post_set.aggregate(pcr=Coalesce(Sum('comment__rating'), 0)).get('pcr')

        print(posts_rating)
        print('----------------')
        print(comments_rating)
        print('----------------')
        print(posts_comments_rating)

        self.rating = posts_rating * 3 + comments_rating + posts_comments_rating
        self.save()



class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)



class Post(models.Model):
    paper = 'PA'
    news = 'NS'

    CHOICES = [
        (paper, 'Статья'),
        (news, 'Новость')
    ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categorys =  models.ManyToManyField(Category, through='PostCategory')
    choice = models.CharField(max_length=2, choices=CHOICES, default=news)
    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like (self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'



class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)


    def like (self):
        self.rating +=1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()