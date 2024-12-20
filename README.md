
# Proyecto de Programación Backend

## Descripción
Este proyecto fue desarrollado como parte de la cuarta evaluación de Programación Backend. Es un sistema CRUD diseñado para organizar datos relacionados con **Clases**, **Profesores** y **Estudiantes**, cada uno con sus respectivas funcionalidades.

---

## Instalación

### Clonar el repositorio
Clona el proyecto con el siguiente comando:
```bash
git clone https://github.com/ScarlettRosse/Back_end.git
```

---

## Requisitos del Sistema

- **Django:** Versión 5.1.1
- **Python:** Versión 3.12.4

### Instalación de Dependencias

1. Para instalar Django:
   ```bash
   pip install django
   ```

2. Para verificar la versión de Django instalada:
   ```bash
   python -m django --version
   ```
   Debe devolver: `5.1.1`.

---

## Inicialización del Proyecto

1. **Inicia el proyecto con:**
   ```bash
   django-admin startproject nombre_del_proyecto
   ```

2. **Crea las aplicaciones con:**
   ```bash
   python manage.py startapp nombre_de_la_aplicacion
   ```

---

## Estructura del Proyecto

### Características de las Aplicaciones
- Funcionalidades **CRUD** completas.
- Templates organizados en carpetas para **CSS** e **Imágenes**, manteniendo orden y limpieza.

### Configuración de `settings.py`
1. En la sección `TEMPLATES > DIRS`, agrega:
   ```python
   [BASE_DIR / "templates"]
   ```

2. Registra las aplicaciones en la sección `INSTALLED_APPS` de `settings.py`.

---

## Librerías Utilizadas
- **`django.shortcuts`:** `render`, `redirect`, `get_object_or_404`
- **`django.contrib.auth.decorators`:** `login_required`
- **`django.core.paginator`:** `Paginator`
- **`django.urls`:** `path`

---

## Funcionalidades Principales

### 1. **Agregar Clase**
La función `agregar_clase` captura datos mediante el método `POST`, crea un objeto con ellos y los guarda. Posteriormente, redirige al usuario a la lista para visualizar el nuevo registro.

### 2. **Listar Clase**
La función `listar_clase` obtiene todos los registros y los muestra en una lista HTML paginada, organizados en bloques de 5 elementos.

### 3. **Actualizar Clase**
La función `actualizar_clase` utiliza `get_object_or_404` para recuperar un objeto por su `id`, permite editar sus datos y los guarda con el método `save()`.

### 4. **Eliminar Clase**
La función `eliminar_clase` utiliza `get_object_or_404` para localizar un objeto por su `id` y lo elimina de la base de datos.

---

Este sistema CRUD fue diseñado para garantizar una gestión sencilla y eficaz de los datos, aprovechando las capacidades y herramientas de Django.
