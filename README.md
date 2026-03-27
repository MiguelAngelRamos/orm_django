## Crear proyecto 

```sh
mkdir project_orm
cd project_orm
```

Con tu terminal apuntando a la carpeta ***minimarket_project***


## Crear el entorno virtual 

```sh
python -m venv venv
```

## Activar el entorno virtual 

```sh
.\venv\Scripts\activate
```

## Instalar Django

```sh
pip install django
```


## Creación del Proyecto y la App (DJANGO)

1. Proyecto
```sh
django-admin startproject core .
```

2. la App

```sh
python manage.py startapp app_crud
```

## Las instalaciones a utilizar dentro de este proyecto

1. Variables de entorno
```sh
pip install python-decouple
```
2. Para conectar a postgresql
```sh
pip install psycopg2-binary
```

## Configuracion dentro de "core"

En core/settings.py, debemos registrar la app y configurar las rutas de carpetas

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_crud', # esto es nuestra app
]

```

## Arrancar Proyect Django 

```sh
python manage.py runserver
```


