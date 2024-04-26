#--------creacion de las URLS para las vistas------#

from django.urls import path
from . import views



urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('nosotros',views.nosotros, name='nosotros'),
    path('libros',views.libros, name='libros'),
    path('crear',views.crearLibro, name='crear'),
    path('editar',views.editarLibro, name='editar'),
]