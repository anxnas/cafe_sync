from decimal import Decimal
from typing import Dict, List, Optional, Union, Any
from django.db.models import Sum
from loguru import logger

from api.models import Order, OrderStatus
from api.exceptions.order_exceptions import InvalidOrderData

class OrderService:
    """
    Сервис для работы с заказами.
    """
    
    @staticmethod
    def create_order(table_number: int, items: List[Dict[str, Any]], status: str = OrderStatus.PENDING) -> Order:
        """
        Создает новый заказ.
        """
        try:
            # Валидация данных
            if table_number <= 0:
                raise InvalidOrderData("Номер стола должен быть положительным числом")
            
            if not items:
                raise InvalidOrderData("Список блюд не может быть пустым")
            
            # Проверка структуры каждого элемента в списке items
            for item in items:
                if not isinstance(item, dict):
                    raise InvalidOrderData("Каждое блюдо должно быть объектом")
                
                if 'name' not in item:
                    raise InvalidOrderData("Каждое блюдо должно содержать поле 'name'")
                
                if 'price' not in item:
                    raise InvalidOrderData("Каждое блюдо должно содержать поле 'price'")
                
                try:
                    price = float(item['price'])
                    if price <= 0:
                        raise InvalidOrderData("Цена блюда должна быть положительным числом")
                except (ValueError, TypeError):
                    raise InvalidOrderData("Цена блюда должна быть числом")
            
            # Создание заказа
            order = Order(
                table_number=table_number,
                items=items,
                status=status
            )
            order.save()
            
            logger.info(f"Создан новый заказ: {order}")
            return order
            
        except Exception as e:
            logger.error(f"Ошибка при создании заказа: {e}")
            raise
    
    @staticmethod
    def update_order(order_id: str, table_number: Optional[int] = None, 
                    items: Optional[List[Dict[str, Any]]] = None, 
                    status: Optional[str] = None) -> Order:
        """
        Обновляет существующий заказ.
        """
        try:
            order = Order.objects.get(uuid=order_id)
            
            # Обновление полей, если они предоставлены
            if table_number is not None:
                if table_number <= 0:
                    raise InvalidOrderData("Номер стола должен быть положительным числом")
                order.table_number = table_number
            
            if items is not None:
                if not items:
                    raise InvalidOrderData("Список блюд не может быть пустым")
                
                # Проверка структуры каждого элемента в списке items
                for item in items:
                    if not isinstance(item, dict):
                        raise InvalidOrderData("Каждое блюдо должно быть объектом")
                    
                    if 'name' not in item:
                        raise InvalidOrderData("Каждое блюдо должно содержать поле 'name'")
                    
                    if 'price' not in item:
                        raise InvalidOrderData("Каждое блюдо должно содержать поле 'price'")
                    
                    try:
                        price = float(item['price'])
                        if price <= 0:
                            raise InvalidOrderData("Цена блюда должна быть положительным числом")
                    except (ValueError, TypeError):
                        raise InvalidOrderData("Цена блюда должна быть числом")
                
                order.items = items
            
            if status is not None:
                if status not in [choice[0] for choice in OrderStatus.choices]:
                    raise InvalidOrderData(f"Недопустимый статус. Допустимые значения: {[choice[0] for choice in OrderStatus.choices]}")
                order.status = status
            
            order.save()
            
            logger.info(f"Обновлен заказ: {order}")
            return order
            
        except Order.DoesNotExist:
            logger.error(f"Заказ с ID {order_id} не найден")
            raise
        except Exception as e:
            logger.error(f"Ошибка при обновлении заказа: {e}")
            raise
    
    @staticmethod
    def delete_order(order_id: str) -> None:
        """
        Удаляет заказ.
        """
        try:
            order = Order.objects.get(uuid=order_id)
            order_info = str(order)
            order.delete()
            
            logger.info(f"Удален заказ: {order_info}")
            
        except Order.DoesNotExist:
            logger.error(f"Заказ с ID {order_id} не найден")
            raise
        except Exception as e:
            logger.error(f"Ошибка при удалении заказа: {e}")
            raise
    
    @staticmethod
    def change_order_status(order_id: str, status: str) -> Order:
        """
        Изменяет статус заказа.
        """
        try:
            if status not in [choice[0] for choice in OrderStatus.choices]:
                raise InvalidOrderData(f"Недопустимый статус. Допустимые значения: {[choice[0] for choice in OrderStatus.choices]}")
            
            order = Order.objects.get(uuid=order_id)
            order.status = status
            order.save()
            
            logger.info(f"Изменен статус заказа {order} на {status}")
            return order
            
        except Order.DoesNotExist:
            logger.error(f"Заказ с ID {order_id} не найден")
            raise
        except Exception as e:
            logger.error(f"Ошибка при изменении статуса заказа: {e}")
            raise
    
    @staticmethod
    def get_revenue_data() -> Dict[str, Union[Decimal, int, List[Order]]]:
        """
        Получает данные о выручке за оплаченные заказы.
        """
        try:
            # Получаем сумму всех оплаченных заказов
            total_revenue = Order.objects.filter(
                status=OrderStatus.PAID
            ).aggregate(
                total=Sum('total_price')
            )['total'] or Decimal('0.00')
            
            # Получаем количество оплаченных заказов
            paid_orders_count = Order.objects.filter(
                status=OrderStatus.PAID
            ).count()
            
            # Получаем список всех оплаченных заказов
            paid_orders = Order.objects.filter(status=OrderStatus.PAID)
            
            return {
                'total_revenue': total_revenue,
                'paid_orders_count': paid_orders_count,
                'paid_orders': paid_orders
            }
            
        except Exception as e:
            logger.error(f"Ошибка при получении данных о выручке: {e}")
            raise