FROM python:3.9-slim
LABEL authors="37525"

WORKDIR /app

# Устанавливаем переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc python3-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Копируем и устанавливаем зависимости
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем весь проект в рабочую директорию
COPY . .

# Указываем настройки для Django
ENV DJANGO_SETTINGS_MODULE WeatherAPI.settings

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]