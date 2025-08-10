# Florilegium Backend 🌿🛠️

Главный бэкенд для мульти-микросервисного проекта на Django, предоставляющий API для различных сервисов.

-----

### О проекте

Florilegium Backend — это основной бэкенд-сервис, разработанный на **Django** и **Django REST Framework (DRF)**. Он является ключевым компонентом мульти-микросервисной архитектуры проекта "Florilegium", обеспечивая управление данными, аутентификацию и взаимодействие с другими сервисами через RESTful API. Проект ориентирован на масштабируемость, безопасность и чистоту кода.

-----

### Структура проекта 📂

```
.
├── backend
│   ├── api
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── __init__.py
│   │   │   ├── 0001_initial.py
│   │   │   └── 0002_alter_post_photos.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── authentication
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── __init__.py
│   │   │   └── 0001_initial.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── backend
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── settings.cpython-312.pyc
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── manage.py
│   ├── photos
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── __init__.py
│   │   │   ├── 0001_initial.py
│   │   │   └── 0002_remove_post_category_delete_category_delete_post.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── venv
```

-----

### Используемые технологии 🛠️

Проект разработан с использованием следующих ключевых технологий и библиотек:

  * **Python**: Основной язык программирования.
  * **Django**: Высокоуровневый веб-фреймворк для быстрой разработки безопасных и масштабируемых веб-приложений.
  * **Django REST Framework (DRF)**: Мощный и гибкий набор инструментов для создания API на Django.
  * **`djangorestframework-simplejwt`**: Предоставляет JWT-аутентификацию для REST API.
  * **`psycopg2-binary`**: Адаптер PostgreSQL для Python, используемый для работы с базой данных.
  * **`dj-database-url`**: Позволяет удобно настраивать подключения к базам данных из URL-строк.
  * **`python-dotenv`**: Для управления переменными окружения.
  * **`drf-spectacular`**: Генерация интерактивной документации API (OpenAPI/Swagger UI).
  * **`gunicorn`**: Python WSGI HTTP Server для развёртывания Django-приложений.
  * **`django-cors-headers`**: Управление CORS-заголовками для кросс-доменных запросов.
  * **`loguru`**: Удобная библиотека для логирования.
  * **`pydantic`**: Библиотека для валидации данных с использованием аннотаций типов.
  * Прочие: `asgiref`, `aiofiles`, `aiohttp`, `asyncio`, `pytz`, `PyYAML`, `requests` и другие вспомогательные библиотеки.

-----

### Переменные окружения (.env) 🔑

Для корректной работы проекта необходимо настроить переменные окружения. Создайте файл `.env` в корневой директории проекта (`Florilegium_backend/backend/.env`) и заполните его следующими данными:

```env
SECRET_KEY=ВАШ_СЕКРЕТНЫЙ_КЛЮЧ_DJANGO
DEBUG=True/False # Установите False для продакшена
DATABASE_URL=postgres://user:password@host:port/dbname # URL вашей базы данных PostgreSQL
ADMIN_1=email_администратора_1
ADMIN_2=email_администратора_2
```

  * `SECRET_KEY`: Уникальный секретный ключ Django для безопасности.
  * `DEBUG`: Управляет режимом отладки. `True` для разработки, `False` для продакшена.
  * `DATABASE_URL`: URL для подключения к базе данных PostgreSQL.
  * `ADMIN_1`, `ADMIN_2`: Email-адреса администраторов для Django.

-----

### Установка и запуск 🚀

Чтобы запустить бэкенд на своем компьютере, выполните следующие шаги:

1.  **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/Segun228/Florilegium_backend.git
    cd Florilegium_backend/backend
    ```

2.  **Создайте виртуальное окружение и установите зависимости:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для macOS/Linux
    # или
    venv\Scripts\activate     # Для Windows
    pip install -r requirements.txt
    ```

3.  **Примените миграции базы данных:**

    ```bash
    python manage.py migrate
    ```

4.  **Создайте суперпользователя (по желанию, для доступа к Django Admin):**

    ```bash
    python manage.py createsuperuser
    ```

5.  **Запустите сервер разработки:**

    ```bash
    python manage.py runserver
    ```

    Бэкенд будет доступен по адресу `http://127.0.0.1:8000/`.

-----

### Автор проекта ✍️

  * **GitHub**: [@Segun228](https://www.google.com/search?q=https://github.com/Segun228)

-----

### Лицензия 📝

Проект распространяется по лицензии MIT.
