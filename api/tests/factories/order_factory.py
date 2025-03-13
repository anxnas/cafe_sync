import factory
from factory.django import DjangoModelFactory
from api.models import Order, OrderStatus

class OrderFactory(DjangoModelFactory):
    """
    Фабрика для создания тестовых заказов
    """
    class Meta:
        model = Order

    table_number = factory.Sequence(lambda n: n + 1)
    items = factory.List([
        factory.Dict({
            'name': factory.Sequence(lambda n: f'Блюдо {n}'),
            'price': factory.Sequence(lambda n: (n + 1) * 100)
        }) for _ in range(2)
    ])
    status = OrderStatus.PENDING

    @factory.post_generation
    def calculate_total(obj, create, extracted, **kwargs):
        """
        Подсчет общей стоимости заказа после создания
        """
        if create:
            obj.total_price = sum(item['price'] for item in obj.items)
            obj.save() 