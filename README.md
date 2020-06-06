# Django Rest Framework

Primer api rest con Django rest framework.

## Instalar dependencias 

~~~
pip install -r requirements.txt
~~~

## Comandos para Django

~~~
python manage.py makemigrations
~~~

~~~
python manage.py migrate
~~~

~~~
python manage.py collectstatic
~~~


~~~
python manage.py createsuperuser
~~~

Para ejecutar el proyecto:

~~~
python manage.py runserver
~~~

## Funcionamiento

Despues de instalar todas las dependencias, usted debe dirijiese a la
url que se le indica al ejecutar el comando `python manage.py runserver`.

Para saber con que urls hay disponibles dirijase al archivo `urls.py` de la carpeta principal. Allí
encontrara la informacion suficiente al respecto.

Para poder eliminar o editar algun valor desde la api no debe olvidarse de
loguearse con el superusuario que halla creado en el punto anterior. Esto con el proposito de 
agregarle seguridad de escritura a la api en la web. 