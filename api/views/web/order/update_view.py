from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import transaction
from loguru import logger

from api.models import Order
from api.forms import OrderForm

class OrderUpdateView(UpdateView):
    """
    Представление для обновления существующего заказа.
    """
    model = Order
    form_class = OrderForm
    template_name = 'api/order_form.html'
    success_url = reverse_lazy('order-list')
    
    def get_context_data(self, **kwargs):
        """
        Добавляет дополнительные данные в контекст шаблона.
        """
        context = super().get_context_data(**kwargs)
        context['is_update'] = True

        return context
    
    def form_valid(self, form):
        """
        Обрабатывает валидную форму.
        """
        try:
            with transaction.atomic():
                response = super().form_valid(form)
                messages.success(self.request, f'Заказ для стола {self.object.table_number} успешно обновлен.')
                logger.info(f'Обновлен заказ: {self.object}')
                return response
        except Exception as e:
            messages.error(self.request, f'Ошибка при обновлении заказа: {str(e)}')
            logger.error(f'Ошибка при обновлении заказа: {e}')
            return self.form_invalid(form)