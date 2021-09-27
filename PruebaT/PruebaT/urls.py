"""PruebaT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from principal.views import inicio, crearpelicula, crearticket, editarpelicula, eliminarpelicula, editarticket, eliminarticket

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('crearpelicula/', crearpelicula, name='crearticket'),
    path('crearticket/', crearticket, name='crearpelicula'),
    path('editarpelicula/<int:id>', editarpelicula, name='editarpelicula' ),
    path('eliminarpelicula/<int:id>', eliminarpelicula, name="eliminarpelicula"),
    path('editarticket/<int:id>', editarticket, name='editarticket' ),
    path('eliminarticket/<int:id>', eliminarticket, name="eliminarticket"),
]
