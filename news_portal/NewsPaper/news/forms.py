from django.forms import ModelForm
from .models import Post, Category

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['headline', 'author', 'content', 'categories', 'art_or_nw']


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name']


