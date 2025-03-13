import pytest
from api.utils.validators import validate_json_items
from api.exceptions.order_exceptions import InvalidOrderData

class TestJsonValidators:
    def test_valid_json_items(self):
        """
        Тест валидации корректного JSON
        """
        valid_json = '[{"name": "Пицца", "price": 500}, {"name": "Кола", "price": 100}]'
        items = validate_json_items(valid_json)
        assert len(items) == 2
        assert items[0]['name'] == 'Пицца'
        assert items[0]['price'] == 500

    def test_invalid_json_format(self):
        """
        Тест валидации некорректного формата JSON
        """
        invalid_json = 'not a json'
        with pytest.raises(InvalidOrderData):
            validate_json_items(invalid_json)

    def test_invalid_items_structure(self):
        """
        Тест валидации некорректной структуры элементов
        """
        invalid_items = '[{"name": "Пицца"}]'  # Отсутствует цена
        with pytest.raises(InvalidOrderData):
            validate_json_items(invalid_items)

    def test_negative_price(self):
        """
        Тест валидации отрицательной цены
        """
        invalid_items = '[{"name": "Пицца", "price": -500}]'
        with pytest.raises(InvalidOrderData):
            validate_json_items(invalid_items) 