# MyDiego Shop

## Descripción
MyDiego Shop es una aplicación web desarrollada con Django que implementa un sistema de gestión de productos y categorías. La aplicación permite visualizar, crear y gestionar productos organizados por categorías.

## Características
- Listado de productos
- Detalles de productos individuales
- Creación de nuevos productos
- Categorización de productos
- Gestión de imágenes de productos
- Interfaz estilizada con Tailwind CSS

## Estructura del Proyecto
- **shop/**: Aplicación principal que maneja la lógica de productos y categorías
  - `models.py`: Define los modelos de Products y Category
  - `views.py`: Contiene las vistas para listar, mostrar y crear productos
  - `forms.py`: Formularios personalizados para la creación de productos
  - `urls.py`: Configuración de rutas de la aplicación

## Tecnologías Utilizadas
- Django 5.1
- SQLite
- Tailwind CSS
- Python

## Configuración del Proyecto
El proyecto incluye:
- Gestión de archivos estáticos y multimedia
- Sistema de templates de Django
- Formularios personalizados con estilos Tailwind
- Base de datos SQLite

## Modelos
### Category
- Nombre de categoría

### Products
- Nombre
- Descripción
- Precio
- Categoría (ForeignKey)
- Estado activo
- Fecha de creación
- Imagen del producto

## Rutas Principales
- `/`: Página principal
- `/list`: Lista de productos
- `/<id>/`: Detalles del producto
- `/product_form/`: Formulario de creación de productos