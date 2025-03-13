from django import forms
import json

from api.models import Order
from api.utils.validators import validate_json_items

class OrderForm(forms.ModelForm):
    """
    Форма для создания и редактирования заказов с динамическим добавлением блюд.
    """
    
    class Meta:
        model = Order
        fields = ['table_number', 'status']
    
    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        self.items_data = []
        
        if instance and instance.items:
            # Если редактируем существующий заказ, сохраняем данные о блюдах
            self.items_data = instance.items
        
        super().__init__(*args, **kwargs)
    
    def clean(self):
        """
        Валидация формы и обработка данных о блюдах.
        """
        cleaned_data = super().clean()
        
        # Получаем данные о блюдах из POST-запроса
        items = []
        i = 0
        while f'item_name_{i}' in self.data:
            name = self.data.get(f'item_name_{i}')
            price_str = self.data.get(f'item_price_{i}')
            
            if name and price_str:
                try:
                    price = float(price_str)
                    if price <= 0:
                        self.add_error(None, f"Цена блюда '{name}' должна быть положительным числом")
                    else:
                        items.append({
                            'name': name,
                            'price': price
                        })
                except ValueError:
                    self.add_error(None, f"Цена блюда '{name}' должна быть числом")
            
            i += 1
        
        if not items:
            self.add_error(None, "Необходимо добавить хотя бы одно блюдо")
        
        cleaned_data['items'] = items
        return cleaned_data
    
    def save(self, commit=True):
        """
        Сохраняет форму, устанавливая поле items из данных формы.
        """
        instance = super().save(commit=False)
        instance.items = self.cleaned_data['items']
        
        if commit:
            instance.save()
        
        return instance