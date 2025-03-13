import pytest
from decimal import Decimal
from api.services.order_service import OrderService
from api.models import OrderStatus
from api.exceptions.order_exceptions import InvalidOrderData

pytestmark = pytest.mark.django_db

class TestOrderService:
    def test_create_order(self, valid_order_data):
        """
        Тест создания заказа через сервис
        """
        order = OrderService.create_order(**valid_order_data)
        assert order.table_number == valid_order_data['table_number']
        assert order.items == valid_order_data['items']
        assert order.status == OrderStatus.PENDING

    def test_create_order_with_invalid_data(self, invalid_order_data):
        """
        Тест создания заказа с невалидными данными
        """
        with pytest.raises(InvalidOrderData):
            OrderService.create_order(**invalid_order_data)

    def test_update_order(self, pending_order):
        """
        Тест обновления заказа
        """
        new_data = {
            'table_number': 2,
            'items': [{'name': 'Суп', 'price': 300}]
        }
        updated_order = OrderService.update_order(
            order_id=str(pending_order.uuid),
            **new_data
        )
        assert updated_order.table_number == new_data['table_number']
        assert updated_order.items == new_data['items']

    def test_change_order_status(self, pending_order):
        """
        Тест изменения статуса заказа
        """
        updated_order = OrderService.change_order_status(
            order_id=str(pending_order.uuid),
            status=OrderStatus.PAID
        )
        assert updated_order.status == OrderStatus.PAID

    def test_get_revenue_data(self, paid_orders):
        """
        Тест получения данных о выручке
        """
        revenue_data = OrderService.get_revenue_data()
        assert revenue_data['paid_orders_count'] == len(paid_orders)
        assert revenue_data['total_revenue'] > Decimal('0') 