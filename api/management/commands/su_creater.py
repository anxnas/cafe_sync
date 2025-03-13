import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from loguru import logger


class Command(BaseCommand):
    """
    Кастомная команда для создания суперпользователя через переменные окружения.
    Решает проблему создания в неинтерактивном режиме (PyCharm, CI/CD и т.д.)
    """

    help = 'Создает суперпользователя из переменных окружения'

    def handle(self, *args, **options):
        User = get_user_model()
        admin_exists = User.objects.filter(is_superuser=True).exists()

        if admin_exists:
            logger.info('Суперпользователь уже существует')
            return

        admin_email = os.getenv('DJANGO_SUPERUSER_EMAIL')
        admin_password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
        admin_username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')

        if not all([admin_email, admin_password]):
            logger.warning(
                'Не заданы переменные окружения для суперпользователя. '
                'Требуются: DJANGO_SUPERUSER_EMAIL и DJANGO_SUPERUSER_PASSWORD'
            )
            return

        try:
            User.objects.create_superuser(
                username=admin_username,
                email=admin_email,
                password=admin_password
            )
            logger.success(f'Создан суперпользователь: {admin_email}')
        except Exception as e:
            logger.error(f'Ошибка создания суперпользователя: {str(e)}')