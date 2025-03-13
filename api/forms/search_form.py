from django import forms

from api.models import OrderStatus

class OrderSearchForm(forms.Form):
    """
    Форма для поиска заказов.
    
    Attributes:
        table_number: Поле для поиска по номеру стола.
        status: Поле для поиска по статусу.
    """
    table_number = forms.IntegerField(
        required=False,
        label='Номер стола',
        min_value=1
    )
    
    status = forms.ChoiceField(
        choices=[('', '-- Все статусы --')] + list(OrderStatus.choices),
        required=False,
        label='Статус'
    )