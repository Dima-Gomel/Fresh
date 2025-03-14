from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    # permission_classes = (IsAdminUser, )
    search_fields = ['name', 'category', 'price', 'quantity', 'description', 'is_available']
