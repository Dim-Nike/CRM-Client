# Запуск проекта
1.  В первый раз:
1.1 pip install django-admin // установка django
1.2 Создать локальную бд postgrec: name: crm_client password: root
1.3 python3 manage.py createsuperuser // Создание юзера для админки
1.4 python3 manage.py migrate // сделать миграции
1.5 python3 manage.py runserver // запуск проекта

2. В последующие разы:
2.1 python3 manage.py runserver

# CRM-Client
python3 manage.py startapp CRM_api

#Миграции
python3 manage.py makemigrations

python3 manage.py migrate

**create CRM_api**

Удалить БД в консоли => **dropdb CRM_api

#Админка
Создание суперпользователя => **python3 manage.py createsuperuser**
