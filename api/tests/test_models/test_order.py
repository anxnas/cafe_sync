import pytest
from api.models import Order, OrderStatus
from decimal import Decimal

pytestmark = pytest.mark.django_db

class TestOrderModel:
    def test_order_creation(self, pending_order):
        """
        Тест создания заказа
        """
        assert pending_order.pk is not None
        assert pending_order.status == OrderStatus.PENDING
        assert len(pending_order.items) == 2

    def test_total_price_calculation(self):
        """
        Тест расчета общей стоимости заказа
        """
        order = Order.objects.create(
            table_number=1,
            items=[
                {'name': 'Пицца', 'price': 500},
                {'name': 'Кола', 'price': 100}
            ]
        )
        assert order.total_price == Decimal('600.00')

    def test_status_change(self, pending_order):
        """
        Тест изменения статуса заказа
        """
        pending_order.status = OrderStatus.PAID
        pending_order.save()
        assert pending_order.status == OrderStatus.PAID 