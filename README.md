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
3. Приложение будет доступно по адресу: [http://localhost:8000](http://localhost:8000)

#### Без Docker:
1. Убедитесь, что на компьютере установлен Python (версия 3.9+) и [PostgreSQL](https://www.postgresql.org/).
2. Создайте виртуальное окружение и активируйте его:
   ```bash
   python -m venv venv
   source venv/bin/activate  # MacOS/Linux
   venv\Scripts\activate  # Windows
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Выполните миграции базы данных:
   ```bash
   python manage.py migrate
   ```
5. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```
6. Приложение будет доступно по адресу: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

### 3. Настройка переменных окружения

Для корректной работы приложения создайте `.env` файл в корне проекта и добавьте в него следующие переменные (замените значения на свои):
DB_NAME=postgres DB_USER=postgres DB_PASSWORD=securepassword DB_HOST=db DB_PORT=5432 DJANGO_SECRET_KEY=your_secret_key OPENWEATHER_API_KEY=your_api_key DJANGO_DEBUG=True


---

### 4. Дополнительные команды

Если вы развернули проект без Docker:
- Выполните команду `python manage.py collectstatic`, чтобы собрать статические файлы:
  ```bash
  python manage.py collectstatic
  ```
