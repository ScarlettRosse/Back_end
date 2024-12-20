from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from Clase.views import *
from Estudiante.views import *
from Profesor.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', pagina_principal, name='inicio'),
    path('registro/', registro, name='registro'),
# -----------------------clase--------------------------------
    path('add_clase/',agregar_clase, name='crear_clase'),
    path('list_clase/', listar_clase, name='listar_clases'),
    path('actu_clase/<int:id>', actualizar_clase, name='actualizar_clase'),
    path('elim_clase/<int:id>', eliminar_clase, name='eliminar_clase'),
    # # separacion de views de clase
    path('agre_profesor/', agregar_profe, name='crear_prof'),
    path('list_profesor/', listar_profe, name='listar_prof'),
    path('actua_profesor/<int:id>', actualizar_profe, name='actualizar_prof'),
    path('elim_profesor/<int:id>', eliminar_profe, name='eliminar_prof'),
    # # separacion de views de profesor
    path('list_estudiante/', listar_estudiante, name='listar_estudiantes'),
    path('agregar_estudiante/', agregar_estudiante, name='crear_estudiantes'),
    path('actua_estudiante/<int:id>', actualizar_Estudiante, name='actualizar_estudiante'),
    path('elim_estudiante/<int:id>', eliminar_estudiante, name='eliminar_estudiante')
    # # separacion de views estudiantes
]