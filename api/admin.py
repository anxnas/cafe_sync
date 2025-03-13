from django.contrib import admin
from api.models import Order, OrderStatus

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Админка для модели Order.

    Настройки:
        list_display: Поля, отображаемые в списке заказов.
        list_filter: Фильтры для списка заказов.
        search_fields: Поля, по которым можно выполнять поиск.
        readonly_fields: Поля, которые нельзя редактировать.
        fieldsets: Группировка полей в форме редактирования.
    """
    list_display = ('uuid', 'table_number', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('table_number', 'uuid')
    readonly_fields = ('uuid', 'created_at', 'updated_at', 'total_price')

    fieldsets = (
        ('Основная информация', {
            'fields': ('uuid', 'table_number', 'items', 'total_price')
        }),
        ('Статус', {
            'fields': ('status',)
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at')
        }),
    )