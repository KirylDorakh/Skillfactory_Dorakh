from django.contrib import admin
from .models import Post, Author, Category, CategoryUser


# напишем уже знакомую нам функцию обнуления товара на складе
def nullfy_rating_of_post(modeladmin, request, queryset): # все аргументы уже должны быть вам знакомы, самые нужные из них это request — объект хранящий информацию о запросе и queryset — грубо говоря набор объектов, которых мы выделили галочками.
    queryset.update(rating_of_post=0)
nullfy_rating_of_post.short_description = 'Обнулить рейтинг' # описание для более понятного представления в админ панеле задаётся, как будто это объект


class CategoryUserInline(admin.TabularInline):
    model = CategoryUser
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = (CategoryUserInline,)

# создаём новый класс для представления товаров в админке
class PostAdmin(admin.ModelAdmin):

    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['headline', 'rating_of_post', 'author', 'art_or_nw', 'post_time', 'on_top']
    #list_display = [field.name for field in Post._meta.get_fields()] # генерируем список имён всех полей для более красивого отображения
    list_filter = ('art_or_nw', 'author') # добавляем примитивные фильтры в нашу админку
    search_fields = ('headline', 'categories__name')  # тут всё очень похоже на фильтры из запросов в базу, давайте
    actions = [nullfy_rating_of_post]  # добавляем действия в список

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)

#admin.site.unregister(Post)

# Register your models here.
