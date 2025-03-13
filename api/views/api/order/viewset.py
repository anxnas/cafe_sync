from rest_framework import viewsets, status
from rest_framework.response import Response

from api.models import Order, OrderStatus
from api.serializers import OrderSerializer
from api.services.order_service import OrderService
from api.exceptions.order_exceptions import InvalidOrderData
from loguru import logger


class OrderViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с заказами через REST API.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        """
        Получает отфильтрованный queryset на основе параметров запроса.
        """
        queryset = super().get_queryset()
        table_number = self.request.query_params.get('table_number')
        status = self.request.query_params.get('status')

        if table_number:
            queryset = queryset.filter(table_number=table_number)

        if status:
            queryset = queryset.filter(status=status)

        return queryset

    def create(self, request, *args, **kwargs):
        """
        Создает новый заказ.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            order = OrderService.create_order(
                table_number=serializer.validated_data['table_number'],
                items=serializer.validated_data['items'],
                status=serializer.validated_data.get('status', OrderStatus.PENDING)
            )

            return Response(
                self.get_serializer(order).data,
                status=status.HTTP_201_CREATED
            )
        except InvalidOrderData as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, *args, **kwargs):
        """
        Обновляет существующий заказ.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        try:
            order = OrderService.update_order(
                order_id=str(instance.uuid),
                table_number=serializer.validated_data.get('table_number'),
                items=serializer.validated_data.get('items'),
                status=serializer.validated_data.get('status')
            )

            return Response(
                self.get_serializer(order).data
            )
        except InvalidOrderData as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )