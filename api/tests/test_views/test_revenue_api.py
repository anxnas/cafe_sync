import pytest
from rest_framework import status

pytestmark = pytest.mark.django_db

class TestRevenueAPI:
    def test_get_revenue_data(self, api_client, paid_orders):
        """
        Тест получения данных о выручке
        """
        response = api_client.get('/api/revenue/')
        assert response.status_code == status.HTTP_200_OK
        assert 'total_revenue' in response.data
        assert 'paid_orders_count' in response.data
        assert response.data['paid_orders_count'] == len(paid_orders) 