[![Django CI](https://github.com/plzZarbotay/StockMonitor/actions/workflows/django.yml/badge.svg?branch=master)](https://github.com/plzZarbotay/StockMonitor/actions/workflows/django.yml)
# Проект 📈 "Stock Market Monitor"

## Описание проекта

Веб-интерфейс "Stock Market Monitor" разработан для анализа данных рынка в целом. Он предоставляет возможность
парсинга данных о объеме продаж, трендах покупателей и динамике из дня в день. Пользователи могут генерировать красивые
отчеты и анализы на основе этих данных.

## Основные функции

1. **Парсинг данных**: Интерфейс обеспечивает возможность парсинга данных с различных источников, таких как
   онлайн-магазины, социальные сети, новостные сайты и т. д.
2. **Отображение объема продаж**: Пользователи могут просматривать графики и диаграммы, отражающие объем продаж на рынке
   в целом.
3. **Анализ трендов покупателей**: Инструмент анализирует данные о поведении покупателей и помогает выявлять тренды и
   предпочтения.
4. **Динамика из дня в день**: Пользователи имеют возможность отслеживать динамику изменений на рынке изо дня в день с
   помощью наглядных графиков и диаграмм.
5. **Генерация отчетов и аналитики**: Пользователи могут создавать красочные отчеты и аналитические документы на основе
   собранных данных для дальнейшего анализа и представления.

## Установка и запуск проекта (dev-версия)

### Запуск postgres

1. Создать файл `.env` и заполнить его, используя файл `.env.sample` как пример
   ```
   touch .env
   ```
2. Запуск контейнера `pgdb`
   > Если для разработки используются IDE с возможностью запуска контейнеров, то запустить контейнер удобным способом

   Выполнить команду для запуска через консоль:
   ```
   docker compose up -d pgdb
   ```
   > Если нет прав - выполните следующие команды
   ```
   sudo dockerd
   sudo chmod a+rwx /var/run/docker.sock
   sudo chmod a+rwx /var/run/docker.pid
   ```

### Переменные окружения

- `POSTGRES_USER` - имя пользователя в postgres
- `POSTGRES_PASSWORD` - пароль пользователя
- `POSTGRES_DB` - название базы данных
- `POSTGRES_DATA` - путь, по которому будут храниться данные postgres(можно оставить как в `.env.sample`)
- `POSTGRES_PORT` - порт, на котором будет запущена бд на хосте
- `REDIS_PORT` - порт, на котором будет запущен redis

## Техническая документация

### Технологии

- **Язык программирования**: Python, JS
- **Веб-фреймворк**: Django, VueJS
- **Библиотеки для парсинга данных**: requests
- **Библиотеки для анализа данных**: pandas
- **Хранение данных**: PostgreSQL
- **Очереди задач**: Redis

### Структура API

Структура API бэкенда представлена на странице `api/v1/swagger`, доступной после запуска сервера.

## Команда разработчиков
- **Ганяк Александр Олегович**, [телеграм](https://t.me/LemonCompany), тимлид, фронтэнд разработчик
- **Жгенти Дарья Никитична**, [телеграм](https://t.me/dariazh26), фронтэнд разработчик
- **Никольский Константин Германович**, [телеграм](https://t.me/Proksima1), ведущий бэкенд разработчик
- **Гаврилов Никита Валерьевич**, [телеграм](https://t.me/Happ1S), фулстек разработчик
- **Щапов Андрей Денисович**, [телеграм](https://t.me/P691v), бэкенд разработчик

## Лицензия

Этот проект лицензируется по лицензии MIT. Подробности см. в файле [LICENSE](LICENSE).
