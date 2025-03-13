from rest_framework import serializers
from api.models import Order
from api.utils.validators import validate_json_items
from api.exceptions.order_exceptions import InvalidOrderData
import json

class OrderSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Order.
    """
    
    class Meta:
        model = Order
        fields = ['uuid', 'table_number', 'items', 'total_price', 'status', 'created_at', 'updated_at']
        read_only_fields = ['uuid', 'total_price', 'created_at', 'updated_at']
    
    def validate_items(self, value):
        """
        Валидация списка блюд с использованием validate_json_items.
        
        Args:
            value: Список блюд для валидации
            
        Returns:
            List[Dict]: Валидированный список блюд
            
        Raises:
            serializers.ValidationError: Если данные не прошли валидацию
        """
        try:
            # Преобразуем список в JSON-строку и валидируем через validate_json_items
            items_json = json.dumps(value)
            return validate_json_items(items_json)
        except InvalidOrderData as e:
            raise serializers.ValidationError(str(e)) 