from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from loguru import logger

from api.services.order_service import OrderService

class RevenueView(View):
    """
    Представление для отображения выручки за смену.
    """
    
    def get(self, request):
        """
        Обрабатывает GET-запрос для отображения выручки.
        """
        try:
            revenue_data = OrderService.get_revenue_data()
            
            context = {
                'total_revenue': revenue_data['total_revenue'],
                'paid_orders_count': revenue_data['paid_orders_count'],
                'paid_orders': revenue_data['paid_orders']
            }
            
            return render(request, 'api/revenue.html', context)
        except Exception as e:
            messages.error(request, f'Ошибка при получении данных о выручке: {str(e)}')
            logger.error(f'Ошибка при получении данных о выручке: {e}')
            return redirect('order-list')