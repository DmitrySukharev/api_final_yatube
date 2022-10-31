# Проект Yatube API
API для социальной сети блогеров

### Описание
API для соцсети YaTube позволяет работать в ней настоящим программистам.  
Поддерживаются методы GET, POST, PUT, PATCH, DEL для постов и комментариев.  
Для сообществ - метод GET, для подписок - GET & POST.  
Для аутентификации используются JWT-токены и библиотека Djoser.  
Доступна полная документация в формате ReDoc с описанием энд-пойнтов и примерами запросов.  

### Технологии
Python 3.7+  
Django 2.2.16  
Django Rest Framework 3.12.4  
Djoser 2.1.0  

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/DmitrySukharev/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
