# Дневник 

## Описание

**Дневник** — Способ выразить свои мысли, сделать выводы и работу над ошибками, редактировать, удалять, а также просматривать свои записи в удобном интерфейсе. Приложение разработано на основе Django и предоставляет функционал аутентификации пользователей, фильтрации записей и динамического поиска.

## Функционал
- Регистрация и вход для пользователей
- Создание, редактирование и удаление записей дневника
- Поиск записей по заголовку и содержанию
- Фильтрация записей по владельцам
- Реализовано с использованием class-based views (CBV)

## Технологии
- **Backend**: Python, Django
- **Frontend**: HTML, CSS, (добавить любые другие технологии, если используются)
- **База данных**: SQL (по умолчанию, или другая, если используешь)
- **Docker**: контейнеризация для быстрого развёртывания и запуска

## Установка и запуск

### Шаги для локальной установки (без Docker)

1. Клонируйте репозиторий:

    ```bash
   git@github.com:Alexei125/personaldiary.git 
    ```

2. Запустите сервер:

    ```bash
    python manage.py runserver
    ```

Приложение будет доступно по адресу `http://127.0.0.1:8000/`.

### Запуск с использованием Docker

1. Убедитесь, что Docker установлен на вашем компьютере.

2. Клонируйте репозиторий:

    ```bash
   git@github.com:Alexei125/personaldiary.git 
    ```

3. Запустите контейнеры с помощью Docker Compose:

    ```bash
    docker-compose up --build
4. Приложение будет доступно по адресу `http://127.0.0.1:8000/`.

### Переменные окружения

Проект использует следующие переменные окружения, которые можно настроить в файле `.env`:
- `SECRET_KEY` — секретный ключ Django
- `DEBUG` — режим отладки (установите `True` для production)
- `USER` — имя пользователя
- `PASSWORD` — пароль для базы данных
- `PORT` — порт для базы данных
