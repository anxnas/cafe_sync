from django.views.generic import DetailView
from api.models import Order

class OrderDetailView(DetailView):
    """
    Представление для отображения деталей заказа.
    """
    model = Order
    template_name = 'api/order_detail.html'
    context_object_name = 'order'