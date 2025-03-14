from django.db import models


class Product(models.Model):
    # Модель для продуктов (овощей и фруктов).
    objects = None
    name = models.CharField(max_length=200, verbose_name="Название продукта")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество на складе")
    description = models.TextField(blank=True, verbose_name="Описание продукта")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_available = models.BooleanField(default=True, verbose_name="Доступен для продажи")

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
