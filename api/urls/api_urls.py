from django.urls import path, include
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from api.views import OrderViewSet, RevenueAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="Cafe Sync API",
        default_version='v1',
        description="API для системы управления заказами кафе",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@cafe-sync.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

# Создаем роутер для ViewSet
router = DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('revenue/', RevenueAPIView.as_view(), name='api-revenue'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]