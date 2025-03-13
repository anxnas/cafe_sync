from rest_framework.decorators import action
from .viewset import OrderViewSet
from .status_action import change_status

# Добавляем action к OrderViewSet
OrderViewSet.change_status = action(detail=True, methods=['post'])(change_status)

__all__ = ['OrderViewSet']