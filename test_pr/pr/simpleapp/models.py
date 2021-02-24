from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=200)  # имя товара
    price = models.FloatField(validators=[MinValueValidator(0.0, 'Price should be >= 0.0')])  # цена товара
    quantity = models.IntegerField(
        validators=[MinValueValidator(0, 'Quantity should be >= 0')])  # количество товара на складе
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.quantity}'

    def get_absolute_url(self):
        return f'/products/{self.id}'

