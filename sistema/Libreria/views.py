from django.shortcuts import render
from django.http import HttpResponse

#acceso a las paginas del sitio

def inicio (request):
    return render (request, 'Vistas/inicio.html')

def nosotros (request):
    return render (request, 'Vistas/nosotros.html')

#acceso a las libros

def libros (request):
    return render (request,'libros/index.html')

def crearLibro (request):
    return render (request,'libros/crear.html')

def editarLibro (request):
    return render (request,'libros/editar.html')