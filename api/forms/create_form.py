from django import forms
import json

from api.models import Order
from api.utils.validators import validate_json_items

class OrderForm(forms.ModelForm):
    """
    Форма для создания и редактирования заказов.
    
    Attributes:
        items_text: Текстовое поле для ввода блюд в формате JSON.
    """
    items_text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5}),
        label='Список блюд (JSON)',
        help_text='Введите список блюд в формате JSON. Пример: [{"name": "Пицца", "price": 500}, {"name": "Кола", "price": 100}]'
    )
    
    class Meta:
        model = Order
        fields = ['table_number', 'status']
    
    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        
        if instance:
            # Если редактируем существующий заказ, преобразуем JSON в текст
            initial = kwargs.get('initial', {})
            initial['items_text'] = json.dumps(instance.items, ensure_ascii=False, indent=2)
            kwargs['initial'] = initial
        
        super().__init__(*args, **kwargs)
    
    def clean_items_text(self):
        """
        Валидация и преобразование текстового поля items_text в JSON.
        
        Returns:
            list: Список блюд в формате JSON.
        """
        items_text = self.cleaned_data['items_text']
        return validate_json_items(items_text)
    
    def save(self, commit=True):
        """
        Сохраняет форму, устанавливая поле items из items_text.
        
        Args:
            commit: Флаг, указывающий, нужно ли сохранять объект в базе данных.
            
        Returns:
            Order: Объект заказа.
        """
        instance = super().save(commit=False)
        instance.items = self.cleaned_data['items_text']
        
        if commit:
            instance.save()
        
        return instance