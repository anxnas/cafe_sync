from django.db import models
from .base_model import BaseModel
from .status_choices import OrderStatus
from loguru import logger

class Order(BaseModel):
    """
    Модель заказа в кафе.

    Содержит информацию о заказе:
    - table_number: Номер стола.
    - items: Список заказанных блюд с ценами (в формате JSON).
    - total_price: Общая стоимость заказа.
    - status: Статус заказа (в ожидании, готово, оплачено).

    Атрибуты:
        table_number (PositiveIntegerField): Номер стола.
        items (JSONField): Список блюд с ценами.
        total_price (DecimalField): Общая стоимость заказа.
        status (CharField): Статус заказа.

    Методы:
        __str__: Возвращает строковое представление заказа.
        calculate_total: Вычисляет общую стоимость заказа.
        save: Переопределяет метод сохранения для автоматического расчета суммы.
    """
    table_number = models.PositiveIntegerField(verbose_name='Номер стола')
    items = models.JSONField(verbose_name='Список блюд')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общая стоимость')
    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
        verbose_name='Статус'
    )

    def __str__(self) -> str:
        """
        Возвращает строковое представление заказа.

        Возвращает:
            str: Строка в формате "Заказ UUID - Стол НомерСтола".
        """
        return f'Заказ {self.uuid} - Стол {self.table_number}'

    def calculate_total(self) -> None:
        """
        Вычисляет общую стоимость заказа на основе списка блюд.

        Логика:
            - Суммирует цены всех блюд в списке items.
            - Если возникает ошибка (например, отсутствует ключ 'price'), 
              устанавливает total_price = 0 и логирует ошибку.

        Исключения:
            KeyError: Если в items отсутствует ключ 'price'.
            TypeError: Если значение price не является числом.
        """
        try:
            self.total_price = sum(item['price'] for item in self.items)
        except (KeyError, TypeError) as e:
            logger.error(f'Ошибка при расчете суммы заказа: {e}')
            self.total_price = 0

    def save(self, *args, **kwargs) -> None:
        """
        Переопределяет метод сохранения для автоматического расчета суммы.

        Логика:
            - Перед сохранением вызывает метод calculate_total для расчета суммы.
            - Сохраняет запись в базе данных.

        Параметры:
            *args: Позиционные аргументы для метода save.
            **kwargs: Именованные аргументы для метода save.
        """
        self.calculate_total()
        super().save(*args, **kwargs) 