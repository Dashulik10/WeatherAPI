# WeatherAPI

Проект представляет собой простое Django-приложение для работы с погодными данными через OpenWeatherAPI.

## Как загрузить и запустить проект

### 1. Скачивание проекта
Клонируйте репозиторий с GitHub:
```bash
git clone <URL_репозитория>
cd WeatherAPI
```

Или скачайте архив с проектом и разархивируйте его.

---

### 2. Установка зависимостей

#### С помощью Docker:
1. Убедитесь, что у вас установлен Docker и Docker Compose.
2. Запустите проект с помощью команды:
   ```bash
   docker-compose up --build
   ```
Приложение будет доступно по адресу: [http://localhost:8000](http://localhost:8000)


Если вы развернули проект без Docker:
- Выполните команду `python manage.py collectstatic`, чтобы собрать статические файлы:
  ```bash
  python manage.py collectstatic
  ```
