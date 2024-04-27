# StockMonitor backend

## Установка и запуск Django (Инструкция для linux)

1. В папке с backend`ом создать виртуальное окружение
   ```
   python3 -m venv venv
   ```
2. Активировать виртуальное окружение
   ```
   source venv/bin/activate
   ```
3. Установить необходимые зависимости
   ```
   pip install -r requirements/test.txt -r requirements/dev.txt
   ```
4. Создать файл `.env` и заполнить его, используя файл `.env.sample` как пример
   ```
   touch .env
   ```
5. Перейти в папку с django`й
   ```
   cd stockMonitor/
   ```
6. Мигрировать базу данных
   ```
   python manage.py migrate
   ```
7. Запустить сервер
   ```
   python manage.py runserver
   ```
8. Запустить планировщик
   ```
   celery -A stockMonitor beat -l INFO
   ```
9. Запустить worker
   ```
   celery -A stockMonitor worker -l INFO
   ```
## Переменные окружения

- `DJANGO_DEBUG` - `true`, `1`, `t`, если режим отладки, иначе `false`
- `DJANGO_SECRET_KEY` - строка, которая будет использована Django как секретный ключ
- `DJANGO_CORS_HOSTS` - строка, описывающая разрешенные адреса для CORS. Перечисление с помощью `,`
- `DJANGO_ALLOWED_HOSTS` - строка, описывающая позволенные адреса. Перечисление с помощью `,`

## Проверка кода (flake8)

Для проверки кода необходимо:

1. Установить зависимости(если не установлены) из requirements/test.txt
2. Выполнить команду
   ```
   flake8 --verbose .
   ```

## Форматирование с помощью black

1. Выполнить команду
   ```
   black --verbose .
   ```
