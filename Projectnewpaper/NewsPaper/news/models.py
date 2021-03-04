from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    rating_author = models.IntegerField(default=0)
    author = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        posts = Post.objects.filter(author_post=self.id)  # все посты автора
        rating_post = sum([a.rating_post * 3 for a in posts])  # рейтинг каждого поста автора умножен на 3
        rating_comment = sum([a.rating_comment for a in Comment.objects.filter(author_comment=self.author)])
        # сумма лайков/дислайков к комментам автора
        all_to_post_comment_rating = sum([a.rating_comment for a in Comment.objects.filter(post_comment__in=posts)])
        # сумма лайков/дислайков всех комментов к постам автора
        self.rating_author = rating_post + rating_comment + all_to_post_comment_rating
        self.save()

    def __str__(self):
        return self.author.username


class Category(models.Model):
    category_name = models.TextField(unique=True)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    article = 'AR'
    news = 'NW'
    unknown = 'UK'
    POST_TYPE = [(article, 'Статья'), (news, 'Новость'), (unknown, 'Unknown')]

    author_post = models.ForeignKey(Author, on_delete=models.CASCADE)
    type_post = models.CharField(max_length=2, choices=POST_TYPE, default=unknown)
    category_post = models.ManyToManyField(Category, through='PostCategory')
    date_post = models.DateTimeField(auto_now_add=True)
    header_post = models.TextField()
    text_post = models.TextField()
    rating_post = models.IntegerField(default=0)

    def preview(self):
        preview = self.text_post[:124] + '...'
        return preview

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def __str__(self):
        return self.header_post

    def get_absolute_url(self):  # добавим абсолютный путь чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'


class PostCategory(models.Model):
    post_category = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    date_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()

    def __str__(self):
        info = str(self.author_comment.username)
        return info
