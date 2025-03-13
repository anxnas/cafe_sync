from .list_view import OrderListView
from .detail_view import OrderDetailView
from .create_view import OrderCreateView
from .update_view import OrderUpdateView
from .delete_view import OrderDeleteView
from .status_view import OrderChangeStatusView

__all__ = [
    'OrderListView',
    'OrderDetailView',
    'OrderCreateView',
    'OrderUpdateView',
    'OrderDeleteView',
    'OrderChangeStatusView'
]