from .web import (
    OrderListView,
    OrderDetailView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    OrderChangeStatusView,
    RevenueView
)
from .api import OrderViewSet, RevenueAPIView

__all__ = [
    'OrderListView',
    'OrderDetailView',
    'OrderCreateView',
    'OrderUpdateView',
    'OrderDeleteView',
    'OrderChangeStatusView',
    'RevenueView',
    'OrderViewSet',
    'RevenueAPIView'
]