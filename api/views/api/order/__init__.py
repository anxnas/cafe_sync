from rest_framework.decorators import action
from .viewset import OrderViewSet
from .status_action import change_status_action

# Добавляем action к OrderViewSet
OrderViewSet.change_status = action(detail=True, methods=['post'])(change_status_action)

__all__ = ['OrderViewSet']