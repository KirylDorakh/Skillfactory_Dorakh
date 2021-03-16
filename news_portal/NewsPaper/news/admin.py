from django.contrib import admin
from .models import Post, Author, Category, CategoryUser, PostCategory

class CategoryUserInline(admin.TabularInline):
    model = CategoryUser
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = (CategoryUserInline,)

admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)

# Register your models here.
