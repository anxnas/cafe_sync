FROM python:3.10-slim

# Установка зависимостей для сборки
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Установка рабочей директории
WORKDIR /app

# Копирование файлов зависимостей
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода проекта
COPY . .

# Открытие порта
EXPOSE 8000

# Запуск приложения через Uvicorn
CMD ["uvicorn", "cafe_sync.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"] 