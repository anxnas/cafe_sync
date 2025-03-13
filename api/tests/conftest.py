import pytest
from rest_framework.test import APIClient
from .factories.order_factory import OrderFactory
from api.models import OrderStatus

@pytest.fixture
def api_client():
    """
    Фикстура для API клиента
    """
    return APIClient()

@pytest.fixture
def pending_order():
    """
    Фикстура для заказа в статусе "в ожидании"
    """
    return OrderFactory(status=OrderStatus.PENDING)

@pytest.fixture
def paid_orders():
    """
    Фикстура для оплаченных заказов
    """
    return [OrderFactory(status=OrderStatus.PAID) for _ in range(3)]

@pytest.fixture
def valid_order_data():
    """
    Фикстура с валидными данными для создания заказа
    """
    return {
        'table_number': 1,
        'items': [
            {'name': 'Пицца', 'price': 500},
            {'name': 'Кола', 'price': 100}
        ]
    }

@pytest.fixture
def invalid_order_data():
    """
    Фикстура с невалидными данными для создания заказа
    """
    return {
        'table_number': 1,
        'items': [
            {'name': 'Пицца', 'price': -500},  # Отрицательная цена
            {'name': 'Кола'}  # Отсутствует цена
        ]
    } 