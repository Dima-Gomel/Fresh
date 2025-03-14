from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ('brand', 'mark', 'year', 'price_usd')
        fields = '__all__'
