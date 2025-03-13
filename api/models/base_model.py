import uuid
from django.db import models

class BaseModel(models.Model):
    """
    Базовая модель для всех моделей проекта.

    Содержит общие поля, которые должны быть у всех моделей:
    - uuid: Уникальный идентификатор записи (первичный ключ).
    - created_at: Дата и время создания записи.
    - updated_at: Дата и время последнего обновления записи.

    Атрибуты:
        uuid (UUIDField): Уникальный идентификатор записи.
        created_at (DateTimeField): Дата и время создания записи.
        updated_at (DateTimeField): Дата и время последнего обновления записи.

    Методы:
        __str__: Возвращает строковое представление модели.

    Мета:
        abstract (bool): Указывает, что модель является абстрактной.
        ordering (list): Сортировка по умолчанию (по убыванию created_at).
    """
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name='Уникальный идентификатор',
        help_text='Уникальный идентификатор записи.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        help_text='Дата и время создания записи.'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
        help_text='Дата и время последнего обновления записи.'
    )

    class Meta:
        abstract = True
        ordering = ['-created_at']  # Сортировка по умолчанию: сначала новые записи

    def __str__(self) -> str:
        """
        Возвращает строковое представление модели.

        Возвращает:
            str: Строка в формате "ИмяМодели UUID".
        """
        return f'{self.__class__.__name__} {self.uuid}' 