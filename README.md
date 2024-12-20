Back_end
Proyecto para la 4° nota en el ramo de Back End

Se agrego mediante una WebHook la posibilidad de visualizar cada vez que se realizaba un "push", "commit", "merge", "pull" y "merge pull request"

Este proyecto fue hecho para la cuarta evaluación de Programación Backend.

Este proyecto se puede clonar con el comando "git clone https://github.com/ScarlettRosse/Back_end.git".

Este CRUD esta hecho para ordenar datos via software el cual es sobre Clases, profesores y estudiantes cada uno con sus funcionalidades CRUD.

El proyecto es hecho con Django versión 5.1.1 y Python 3.12.4.

Para instalar Django se ocupa el comando "pip install django" y para ver 
su versión se coloca el comando "python -m django --version" con esto
deberia dar como resultado:
. 5.1.1.

Para iniciar el proyecto se necesita ocupar el comando "django-admin startproject "nombre_del_proyecto"" y para empezar a crear las aplicaciones se ocupa "manage.py startapp "nombre_de_la_aplicación".

Cada aplicacion tiene su CRUD y templates donde estan guardados el CSS y Images esto para mantener un orden y limpieza del mismo.

Las librerias importadas y ocupadas son las siguientes:
Desde "django.shortcuts" se importo "render, redirect y get_object_or_404".
Desde "django.contrib.auth.decorators" se importo "login_required".
Desde "django.core.paginator" se importo "Paginator".
Desde "django.urls" se importo "path".
Primero para empezar se inicia con la configuración del "settings.py" donde se copia la variable
"BASE_DIR" y se coloca en TEMPLATES en "DIRS" de la siguiente forma: [BASE_DIR/"templates"] de esta forma se va a buscar la carpeta templates automaticamente.

El siguiente paso es configurar las aplicaciones las cuales se colcan en "INSTALLED_APPS" siguiendo el orden que se ve en esta.

 
// Función agregar clase
    Ocupando como referencia la aplicación Clases se muestra como "agregar_clase" Clas trae todos los modelos de los datos desde "models" para despues hacer un "if" para tomar los datos mediante el metodo POST y guardarlo dentro de variables para despues crear el objeto 
    retornar al usuario a la lista para que vea como se guardaron los datos este a su vez hay un return render el cual manda los datos mediante un diccionario.

// Función listar clase
    Esta funcion lo que hace es traer los datos para mostrarlo mediante una lista hecha en HTML con el paginator el cual esta paginado por 5.

// Función actualizar clase
    Las siguientes funciones de las otras aplicaciones funcionan de la misma manera que Clase.
    Esta funcion es casi lo mismo que el crear con la diferencia de que tiene el get_object_or_404 el cual trae los datos de la clase Clase con sus ids y las siguientes lineas son lo mismo que "crear clase" con la diferencia que esta es para editarlas para despues hacer 
    un "save()" para guardar los datos ya editados.

// Función eliminar clase
    Esta función trae los datos desde la clase Clase con sus ids para ser eliminado.
