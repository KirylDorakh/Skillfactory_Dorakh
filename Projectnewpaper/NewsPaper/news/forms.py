from django.forms import ModelForm
from .models import Post, Author


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['author_post', 'header_post', 'text_post', 'category_post']


class AuthorForm(ModelForm):

    class Meta:
        model = Author
        fields = ['author', 'rating_author']