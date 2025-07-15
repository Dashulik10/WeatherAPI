FROM python:3.9-slim
LABEL authors="37525"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc python3-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE WeatherAPI.settings

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]