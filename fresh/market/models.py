from django.db import models


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=200, verbose_name="Название продукта")
    price = models.FloatField(verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество на складе")
    description = models.TextField(blank=True, verbose_name="Описание продукта")
    is_available = models.BooleanField(default=True, verbose_name="Доступен для продажи")

    def __str__(self):
        return f"{self.name} | {self.price} | {self.quantity}"
