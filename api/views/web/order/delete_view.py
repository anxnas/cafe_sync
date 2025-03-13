from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from loguru import logger

from api.models import Order

class OrderDeleteView(DeleteView):
    """
    Представление для удаления заказа.
    """
    model = Order
    template_name = 'api/order_delete.html'
    success_url = reverse_lazy('order-list')
    
    def delete(self, request, *args, **kwargs):
        """
        Удаляет объект и добавляет сообщение об успешном удалении.
        """
        order = self.get_object()
        messages.success(request, f'Заказ для стола {order.table_number} успешно удален.')
        logger.info(f'Удален заказ: {order}')
        return super().delete(request, *args, **kwargs)