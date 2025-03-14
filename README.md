# Cafe Sync - Система управления заказами кафе

![Cafe Sync Logo](https://dummyimage.com/600x400/000000/0011ff&text=Cafe+Sync)

## Содержание
- [Описание проекта](#описание-проекта)
- [Функциональные возможности](#функциональные-возможности)
- [Технологический стек](#технологический-стек)
- [Установка и запуск](#установка-и-запуск)
- [API документация](#api-документация)
- [Веб-интерфейс](#веб-интерфейс)
- [Тестирование](#тестирование)
- [Лицензия](#лицензия)
- [Контакты](#контакты)

## Описание проекта

Cafe Sync - это система управления заказами для кафе и ресторанов, разработанная с использованием Django и Django REST Framework. Система позволяет эффективно управлять заказами, отслеживать их статус и анализировать выручку.

Проект включает в себя как веб-интерфейс для персонала кафе, так и REST API для интеграции с мобильными приложениями и другими системами.

## Функциональные возможности

### Управление заказами
- Создание новых заказов с указанием номера стола и списка блюд
- Просмотр списка всех заказов с возможностью фильтрации
- Детальный просмотр информации о заказе
- Редактирование существующих заказов
- Удаление заказов
- Изменение статуса заказа (в ожидании, готовится, готов, оплачен, отменен)

### Аналитика
- Просмотр общей выручки
- Количество оплаченных заказов
- Средний чек

### API
- Полноценный REST API для всех операций с заказами
- Документация API с использованием Swagger

## Технологический стек

- Python 3.9+
- Django 5+
- Django REST Framework
- PostgreSQL
- Nginx
- HTML5, CSS3, JavaScript
- Bootstrap 5

### Инструменты разработки
- Docker и Docker Compose
- Git
- Pytest (тестирование)
- Loguru (логирование)

## Установка и запуск

### Установка

1. Клонирование репозитория:
```bash
git clone https://github.com/anxnas/cafe_sync.git
cd cafe_sync
```

2. Создание и активация виртуального окружения:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. Установка зависимостей:
```bash
pip install -r requirements/*.txt (Установить конкретный при необходимости)
```

4. Создание файла .env на основе example.env:
```bash
cp example.env .env
# Отредактируйте .env файл, указав настройки вашей базы данных и другие параметры
```

5. Применение миграций:
```bash
python manage.py migrate
```

6. Создание суперпользователя:
```bash
# Для ручного ввода
python manage.py createsuperuser
# Для PyCharm, CI/CD (предварительно добавить переменные в .env)
python manage.py su_creater
```

### Запуск с использованием Docker

1. Сборка и запуск контейнеров:
```bash
docker-compose up --build
```

## API документация

API документация доступна через Swagger UI и ReDoc:

- Swagger UI: `/api/swagger/`
- ReDoc: `/api/redoc/`
- OpenAPI спецификация: `/api/swagger.json`

### Основные эндпоинты

#### Заказы

| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| GET | `/api/orders/` | Получить список всех заказов |
| POST | `/api/orders/` | Создать новый заказ |
| GET | `/api/orders/{uuid}/` | Получить детали заказа |
| PUT | `/api/orders/{uuid}/` | Обновить заказ полностью |
| PATCH | `/api/orders/{uuid}/` | Обновить заказ частично |
| DELETE | `/api/orders/{uuid}/` | Удалить заказ |
| POST | `/api/orders/{uuid}/change_status/` | Изменить статус заказа |

#### Выручка

| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| GET | `/api/revenue/` | Получить информацию о выручке |

### Примеры запросов

#### Создание заказа

```json
POST /api/orders/
{
  "table_number": 5,
  "items": [
    {
      "name": "Пицца Маргарита",
      "price": 500
    },
    {
      "name": "Кола",
      "price": 100
    }
  ],
  "status": "pending"
}
```

#### Изменение статуса заказа

```json
POST /api/orders/550e8400-e29b-41d4-a716-446655440000/change_status/
{
  "status": "completed"
}
```

## Веб-интерфейс

Веб-интерфейс предоставляет следующие страницы:

- **Список заказов** (`/`): Отображает все заказы с возможностью фильтрации по номеру стола и статусу
- **Создание заказа** (`/order/create/`): Форма для создания нового заказа
- **Детали заказа** (`/order/{uuid}/`): Подробная информация о заказе с возможностью изменения статуса
- **Редактирование заказа** (`/order/{uuid}/update/`): Форма для редактирования заказа
- **Удаление заказа** (`/order/{uuid}/delete/`): Страница подтверждения удаления заказа
- **Выручка** (`/revenue/`): Страница с информацией о выручке

## Тестирование

### Запуск тестов

```bash
# Запуск всех тестов
pytest

# Запуск тестов с покрытием
pytest --cov=api

# Запуск конкретного теста
pytest api/tests/test_models.py
```

## Лицензия

Этот проект распространяется под лицензией MIT. См. файл LICENSE для получения дополнительной информации.

## Контакты

- Разработчик: anxnas (Хренов Святослав Валерьевич)
- Тг канал: https://t.me/anxnas

2025 год