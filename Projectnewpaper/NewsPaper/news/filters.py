from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post


# создаём фильтр
class PostFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля
    # по которым будет фильтроваться (т.е. подбираться) информация о товарах
    class Meta:
        model = Post
        fields = {
            'author_post': ['in'],
            #
            'date_post': ['date__gt'],  #
            'header_post': ['icontains'],  #
        }
        # поля которые мы будем фильтровать (т.е. отбирать по каким-то критериям, имена берутся из моделей)


# создаём фильтр
class PostFilterView(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля
    # по которым будет фильтроваться (т.е. подбираться) информация о товарах
    class Meta:
        model = Post
        fields = {
            'header_post': ['icontains'],
            #
            'date_post': ['date__gt'],  #
            'text_post': ['in'],  #
        }
