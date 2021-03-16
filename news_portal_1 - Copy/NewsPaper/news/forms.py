from django.forms import ModelForm, Form, CharField, IntegerField, EmailField
from .models import Post, Author

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['headline', 'author', 'content', 'categories', 'art_or_nw']

