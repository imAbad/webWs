"""wsRealWeb33 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
#from wsRealWeb33.views import bienvenida, inicio, pruebaHtml, plantillaPrueba, plantillaParametros, plantillaCargador, plantillaShorcut
from wsRealWeb33.views import index, about, acapulcoGolden, agents, contact, services, property

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('bienvenida/', bienvenida),
    #  path('inicio/', inicio),
    # path('pruebaHtml/<nombre>/<int:edad>', pruebaHtml),
    #path('plantillaPrueba/', plantillaPrueba),
    #path('plantillaParametros/', plantillaParametros),
    #path('plantillaCargador', plantillaCargador),
    #path('plantillaShort/', plantillaShorcut),
    path('', index),
    path('about/', about),
    path('acapulcoGolden/', acapulcoGolden),
    path('agents/', agents),
    path('contact/', contact),
    path('services/', services),
    path('property/', property),


]
