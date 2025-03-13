from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Order
from api.services.order_service import OrderService
from api.exceptions.order_exceptions import InvalidOrderData


def change_status_action(self, request, pk=None):
    """
    Изменяет статус заказа.

    Этот метод предназначен для использования как action в OrderViewSet.
    """
    status_value = request.data.get('status')

    if not status_value:
        return Response(
            {"error": "Необходимо указать статус."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        order = OrderService.change_order_status(
            order_id=pk,
            status=status_value
        )

        return Response(
            self.get_serializer(order).data
        )
    except Order.DoesNotExist:
        return Response(
            {"error": "Заказ не найден."},
            status=status.HTTP_404_NOT_FOUND
        )
    except InvalidOrderData as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )