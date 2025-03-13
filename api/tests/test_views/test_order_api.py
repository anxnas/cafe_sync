import pytest
from rest_framework import status
from api.models import Order, OrderStatus

pytestmark = pytest.mark.django_db

class TestOrderAPI:
    def test_create_order(self, api_client, valid_order_data):
        """
        Тест создания заказа через API
        """
        response = api_client.post('/api/orders/', valid_order_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Order.objects.count() == 1
        assert response.data['table_number'] == valid_order_data['table_number']

    def test_create_invalid_order(self, api_client, invalid_order_data):
        """
        Тест создания невалидного заказа через API
        """
        response = api_client.post('/api/orders/', invalid_order_data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_get_order_list(self, api_client, pending_order):
        """
        Тест получения списка заказов
        """
        response = api_client.get('/api/orders/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_get_order_detail(self, api_client, pending_order):
        """
        Тест получения деталей заказа
        """
        response = api_client.get(f'/api/orders/{pending_order.uuid}/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['uuid'] == str(pending_order.uuid)

    def test_update_order(self, api_client, pending_order):
        """
        Тест обновления заказа
        """
        update_data = {
            'table_number': 5,
            'items': [{'name': 'Новое блюдо', 'price': 400}]
        }
        response = api_client.put(
            f'/api/orders/{pending_order.uuid}/',
            update_data,
            format='json'
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data['table_number'] == update_data['table_number']

    def test_change_order_status(self, api_client, pending_order):
        """
        Тест изменения статуса заказа
        """
        response = api_client.post(
            f'/api/orders/{pending_order.uuid}/change_status/',
            {'status': OrderStatus.PAID},
            format='json'
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data['status'] == OrderStatus.PAID 