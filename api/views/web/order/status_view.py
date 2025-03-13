from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from loguru import logger

from api.models import Order, OrderStatus

class OrderChangeStatusView(View):
    """
    Представление для изменения статуса заказа.
    """
    
    def post(self, request, pk):
        """
        Обрабатывает POST-запрос для изменения статуса заказа.
        """
        order = get_object_or_404(Order, pk=pk)
        status_value = request.POST.get('status')
        
        if status_value in [choice[0] for choice in OrderStatus.choices]:
            order.status = status_value
            order.save()
            messages.success(request, f'Статус заказа для стола {order.table_number} изменен на "{OrderStatus(status_value).label}".')
            logger.info(f'Изменен статус заказа {order}: {status_value}')
        else:
            messages.error(request, 'Некорректный статус.')
            logger.error(f'Попытка установить некорректный статус для заказа {order}: {status_value}')
        
        return redirect('order-detail', pk=pk)