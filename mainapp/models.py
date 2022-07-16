# Работа с таблицами(БД)
"""
Типы моделей:
    models.CharField - Строка
    models.TextField - Строка для большого текста
    models.ImageField - Изображения
    models.IntegerField - Целочисленные значения
    models.DecimalField - Вещественные значения
    models.PositiveIntegerField - Целочисленные положительные значения
    models.ForeignKey - Привязка по ключу
        on_delete=models.CASCADE - При удалении категории удаляет все связанные товары
        on_delete=models.PROTECT - Не позволяет удалить, если есть связка по ключу
Методы QuerySet:
    all() - возвращает список всех объектов из БД
    filter() - возвращает список объектов по определенному признаку
    get() - возвращает объект из БД
    create() - создает объект в БД
Пример:
    ProductCategory.objects.all()
"""
from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='product_image', blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.category}'
