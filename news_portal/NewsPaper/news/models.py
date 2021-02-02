from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    rating_of_author = models.FloatField(default=0.0)

    def update_rating(self):
        pass


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article_or_news = models.BooleanField(default=False)
    # False - article, True - news
    post_time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    post_text = models.TextField()
    rating_of_post = models.FloatField(default=0.0)

    categories = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        return self.rating_of_post + 1

    def dislike(self):
        return self.rating_of_post - 1

    def preview(self):
        return self.post_text[0, 123] + "..."


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    comment_text = models.TextField()
    comment_time_in = models.DateTimeField(auto_now_add=True)
    rating_of_comment = models.FloatField(default=0.0)

    def like(self):
        return self.rating_of_comment + 1

    def dislike(self):
        return self.rating_of_comment - 1
