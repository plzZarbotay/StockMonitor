# StockMonitor backend

## Установка и запуск (Инструкция для linux)

1. В папке с backend`ом создать виртуальное окружение
   ```
   python -m venv venv
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

## Тестирование кода
Для тестирования необходимо:
1. Перейти в папку с django`й
   ```
   cd stockMonitor/
   ```
2. Запустить тесты
   ```
   python manage.py test
   ```
   P.S. Для тестирования отдельного приложения необходимо запустить команду
   ```
   python manage.py test [app_name]
   ```
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
