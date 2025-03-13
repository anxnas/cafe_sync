from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import views, status
from rest_framework.response import Response
from loguru import logger
from api.services.order_service import OrderService


class RevenueAPIView(views.APIView):
    """
    API представление для получения информации о выручке.
    """

    @swagger_auto_schema(
        operation_description="Получить информацию о выручке",
        responses={
            200: openapi.Response(
                description="Успешный ответ",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'total_revenue': openapi.Schema(
                            type=openapi.TYPE_NUMBER,
                            description="Общая сумма выручки"
                        ),
                        'paid_orders_count': openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description="Количество оплаченных заказов"
                        ),
                    }
                )
            ),
            500: "Внутренняя ошибка сервера"
        }
    )
    def get(self, request):
        """
        Возвращает общую выручку за оплаченные заказы.
        """
        try:
            revenue_data = OrderService.get_revenue_data()

            return Response({
                'total_revenue': revenue_data['total_revenue'],
                'paid_orders_count': revenue_data['paid_orders_count']
            })
        except Exception as e:
            logger.error(f"Ошибка при получении данных о выручке: {e}")
            return Response(
                {"error": "Произошла ошибка при получении данных о выручке."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )