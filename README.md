# Nginx Log Analyzer

## Описание

Nginx Log Analyzer — это Django-приложение для обработки и агрегации логов Nginx. Приложение предоставляет возможность парсинга лог-файлов определенного формата, сохранения данных в базу данных, а также их отображения через Django Admin и API на основе Django Rest Framework (DRF).

## Основные функции

- **Парсинг логов Nginx:** Приложение поддерживает парсинг лог-файлов большого размера (до 1 Гб) и сохранение данных в базе данных.
- **Django Admin:** Веб-интерфейс для просмотра и фильтрации логов.
- **API на основе DRF:** Возможность получать, фильтровать и искать данные логов через API. Поддержка пагинации.
- **Swagger:** Документация API через Swagger.

## Технологии
* Python
* Django, DRF
* DRF-YASG
* PostgreSQL
---
## Установка

### Клонирование репозитория
```bash
git clone https://github.com/denimani/NginxLogAnalyzer.git
```
### Запуск проекта в Docker:
_Для работы с переменными окружениями необходимо создать файл .env и заполнить его согласно файлу .env.example:_
```
SECRET_KEY=

# настройка базы данных
POSTGRES_NAME=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
```
_Для создания образа из Dockerfile и запуска контейнера запустить команду:_
```
docker-compose up --build
```
_или_
```
docker-compose up -d --build
```
_Второй вариант для запуска в фоновом режиме._

### Запуск приложения в локальной сети:
_Для запуска проекта необходимо клонировать репозиторий и создать и активировать виртуальное окружение:_ 
```
python3 -m venv venv

source venv/bin/activate
```
_Установить зависимости:_
```
pip install -r requirements.txt
```
_Для работы с переменными окружениями необходимо создать файл .env и заполнить его согласно файлу .env.sample:_
```
SECRET_KEY=

# настройка базы данных
POSTGRES_NAME=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
```
_Выполнить миграции:_
```
python3 manage.py migrate
```
_Для заполнения БД запустить команду:_

```
python3 manage.py parse_nginx_logs nginx_json_logs.txt 
```

_Для создания администратора запустить команду:_

```
python3 manage.py createsuperuser
```

_Для запуска приложения:_

```
python3 manage.py runserver
```

_Для тестирования проекта запустить команду:_

```
python3 manage.py test
```

_Для запуска подсчета покрытия и вывода отчет запустить команды:_

```
coverage run --source='./logparser' manage.py test

coverage report
```

Документация проекта: http://127.0.0.1:8000/swagger/

