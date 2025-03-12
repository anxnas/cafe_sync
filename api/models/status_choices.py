from django.db import models

class OrderStatus(models.TextChoices):
    """
    Статусы заказа.

    Варианты:
        PENDING: Заказ в ожидании.
        READY: Заказ готов.
        PAID: Заказ оплачен.
    """
    PENDING = 'pending', 'В ожидании'
    READY = 'ready', 'Готово'
    PAID = 'paid', 'Оплачено' 