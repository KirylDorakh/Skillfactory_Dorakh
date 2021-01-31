from django.db import models


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    rating_of_author = models.FloatField(default=0.0)


class Category(models.Model):
    name = models.CharField(max_length=255)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article_or_news = models.BooleanField(default = False)
    post_time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    post_text = models.TextField()
    rating_of_post = models.FloatField(default=0.0)

    categories = models.ManyToManyRel(Category, through='PostCategory')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    comment_text = models.TextField()
    comment_time_in = models.DateTimeField(auto_now_add=True)
    rating_of_comment = models.FloatField(default=0.0)
