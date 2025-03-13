from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import transaction
from loguru import logger

from api.models import Order
from api.forms import OrderForm

class OrderCreateView(CreateView):
    """
    Представление для создания нового заказа.
    """
    model = Order
    form_class = OrderForm
    template_name = 'api/order_form.html'
    success_url = reverse_lazy('order-list')
    
    def form_valid(self, form):
        """
        Обрабатывает валидную форму.
        """
        try:
            with transaction.atomic():
                response = super().form_valid(form)
                messages.success(self.request, f'Заказ для стола {self.object.table_number} успешно создан.')
                logger.info(f'Создан новый заказ: {self.object}')
                return response
        except Exception as e:
            messages.error(self.request, f'Ошибка при создании заказа: {str(e)}')
            logger.error(f'Ошибка при создании заказа: {e}')
            return self.form_invalid(form)