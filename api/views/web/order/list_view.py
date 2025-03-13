from django.views.generic import ListView
from api.models import Order
from api.forms import OrderSearchForm

class OrderListView(ListView):
    """
    Представление для отображения списка заказов.
    """
    model = Order
    template_name = 'api/order_list.html'
    context_object_name = 'orders'
    
    def get_queryset(self):
        """
        Получает отфильтрованный queryset на основе параметров запроса.
        """
        queryset = super().get_queryset()
        
        # Получаем параметры фильтрации из GET-запроса
        table_number = self.request.GET.get('table_number')
        status = self.request.GET.get('status')
        
        # Применяем фильтры, если они указаны
        if table_number:
            queryset = queryset.filter(table_number=table_number)
        
        if status:
            queryset = queryset.filter(status=status)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        """
        Добавляет дополнительные данные в контекст шаблона.
        """
        context = super().get_context_data(**kwargs)
        context['search_form'] = OrderSearchForm(self.request.GET or None)
        return context