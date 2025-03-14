# Generated by Django 5.0.4 on 2025-03-13 14:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Уникальный идентификатор записи.', primary_key=True, serialize=False, verbose_name='Уникальный идентификатор')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата и время создания записи.', verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Дата и время последнего обновления записи.', verbose_name='Дата обновления')),
                ('table_number', models.PositiveIntegerField(verbose_name='Номер стола')),
                ('items', models.JSONField(verbose_name='Список блюд')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Общая стоимость')),
                ('status', models.CharField(choices=[('pending', 'В ожидании'), ('ready', 'Готово'), ('paid', 'Оплачено')], default='pending', max_length=20, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-created_at'],
            },
        ),
    ]
