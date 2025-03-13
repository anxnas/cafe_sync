import json
from typing import Any, Dict, List

from api.exceptions.order_exceptions import InvalidOrderData


def validate_json_items(items_json: str) -> List[Dict[str, Any]]:
    """
    Валидирует JSON-строку с элементами заказа.

    Args:
        items_json: JSON-строка с элементами заказа.

    Returns:
        List[Dict[str, Any]]: Список элементов заказа.

    Raises:
        InvalidOrderData: Если JSON-строка некорректна или не соответствует ожидаемому формату.
    """
    try:
        items = json.loads(items_json)

        if not isinstance(items, list):
            raise InvalidOrderData("Список блюд должен быть массивом")

        for item in items:
            if not isinstance(item, dict):
                raise InvalidOrderData("Каждое блюдо должно быть объектом")

            if 'name' not in item:
                raise InvalidOrderData("Каждое блюдо должно содержать поле 'name'")

            if 'price' not in item:
                raise InvalidOrderData("Каждое блюдо должно содержать поле 'price'")

            try:
                price = float(item['price'])
                if price <= 0:
                    raise InvalidOrderData("Цена блюда должна быть положительным числом")
            except (ValueError, TypeError):
                raise InvalidOrderData("Цена блюда должна быть числом")

        return items
    except json.JSONDecodeError:
        raise InvalidOrderData("Некорректный формат JSON")