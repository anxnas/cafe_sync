from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import OrderViewSet, RevenueAPIView

# Создаем роутер для ViewSet
router = DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('revenue/', RevenueAPIView.as_view(), name='api-revenue'),
]