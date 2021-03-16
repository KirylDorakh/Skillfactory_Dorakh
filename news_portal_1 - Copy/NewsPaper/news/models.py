
from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    rating_of_author = models.IntegerField(default=0)


    def update_rating(self):
        posts = Post.objects.filter(author=self.id)
        post_raiting = sum([r.rating_of_post * 3 for r in posts])
        comments = Comment.objects.filter(user=self.id)
        comment_raiting = sum([c.rating_of_comment for c in comments])
        all_to_post_comment_raiting = sum([r.rating_of_comment for r in Comment.objects.filter(post__in=posts)])
        self.rating_of_author = post_raiting + comment_raiting + all_to_post_comment_raiting
        self.save()

    def __str__(self):
        author_id = str(self.user.username)
        return author_id


class Category(models.Model):

    subscribers = models.ManyToManyField(User, through='CategoryUser')
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    news = "NW"
    article = "AR"
    CAT = [(news, "Новость"), (article, 'Статья')]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    art_or_nw = models.CharField(max_length=2,
                            choices=CAT,
                            default=news)
    post_time = models.DateTimeField(auto_now_add=True)
    headline = models.CharField(max_length=255)
    content = models.TextField()
    rating_of_post = models.IntegerField(default=0)

    categories = models.ManyToManyField(Category, through='PostCategory')

    def __str__(self):
        return self.headline

    def like(self):
        self.rating_of_post = self.rating_of_post + 1
        self.save()

    def dislike(self):
        self.rating_of_post = self.rating_of_post - 1
        self.save()

    def preview(self):
        return self.content[:123] + "..."


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class CategoryUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    comment_text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    rating_of_comment = models.IntegerField(default = 0)

    def like(self):
        self.rating_of_comment = self.rating_of_comment + 1
        self.save()

    def dislike(self):
        self.rating_of_comment = self.rating_of_comment - 1
        self.save()

    def __str__(self):
        return self.comment_text
