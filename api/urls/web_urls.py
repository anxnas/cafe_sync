from django.urls import path
from api.views import (
    OrderListView,
    OrderDetailView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    OrderChangeStatusView,
    RevenueView
)

urlpatterns = [
    path('', OrderListView.as_view(), name='order-list'),
    path('order/<uuid:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('order/create/', OrderCreateView.as_view(), name='order-create'),
    path('order/<uuid:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('order/<uuid:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
    path('order/<uuid:pk>/change-status/', OrderChangeStatusView.as_view(), name='order-change-status'),
    path('revenue/', RevenueView.as_view(), name='revenue'),
]