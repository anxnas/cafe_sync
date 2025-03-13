from django.views.generic import DetailView
from api.models import Order, OrderStatus

class OrderDetailView(DetailView):
    """
    Представление для отображения деталей заказа.
    """
    model = Order
    template_name = 'api/order_detail.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        """
        Добавляет в контекст список доступных статусов заказа.
        """
        context = super().get_context_data(**kwargs)
        # Добавляем список всех возможных статусов
        context['available_statuses'] = OrderStatus.choices
        return context