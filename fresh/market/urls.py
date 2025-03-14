from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet

router = routers.DefaultRouter()
router.register('market', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth', include('rest_framework.urls'))
]
