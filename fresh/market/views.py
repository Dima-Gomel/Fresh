from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework import filters


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['name', 'price', 'quantity', 'description', 'is_available']
    filter_backends = [filters.SearchFilter]
