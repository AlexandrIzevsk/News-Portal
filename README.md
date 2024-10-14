Команды:
1) Создать двух пользователей (с помощью метода User.objects.create_user('username')):
   user1 = User.objects.create.user('Alex')
   user2 = User.objects.create.user('AVladimir')
2) Создать два объекта модели Author, связанные с пользователями:
   author1 = Author.objects.create(user=user1)
   ...
3) Добавить 4 категории в модель Category.
   cat1 = Category.objects.create(name='sport')
   ...
4) Добавить 2 статьи и 1 новость.
   post1 = Post.objects.create(author=author1, choice=Post.paper, title='some title', text='some text')
   ...
   post1 = Post.objects.create(author=author1, choice=Post.news, title='some title', text='some text')
5) Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
   post1.categorys.add(cat1, cat2)
   ...
6)Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
   comment1 = Comment.objects.create(post=post1, user=author2, text='some text')
   ...
7) Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
  post1.like()
  ...
  post1.dislike()
  ...
8) Обновить рейтинги пользователей.
  author1.update_rating()
9) Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
  Author.objects.all().order_by('-raitng').values('user__username', 'raiting')[0]
10) Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
  Post.objects.filter(choice='PA').order_by('-raiting').values('time_in__date', 'author__user__username', 'raiting', 'title')[0]
  Post.objects.filter(choice='PA').order_by('-raiting')[0].preview()
12) Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
  Post.objects.filter(choice='PA').order_by('-raiting').values('comment'_time_in__date', 'comment_user__username', 'comment__raiting', 'comment__text')[0]
  
