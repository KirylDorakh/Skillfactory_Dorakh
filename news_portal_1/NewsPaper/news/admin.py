from django.contrib import admin

from .models import Post, Author, Category, PostCategory, CategoryUser

class CategoryUserInline(admin.TabularInline):
    model = CategoryUser
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = (CategoryUserInline,)

class UserAdmin(admin.ModelAdmin):
    inlines = (CategoryUserInline,)

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PostCategory)

# Register your models here.
