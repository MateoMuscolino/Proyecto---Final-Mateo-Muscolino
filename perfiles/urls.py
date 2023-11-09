from django.urls import path
from . import views

urlpatterns = [
    path('', views.mi_pagina, name='mi_pagina'),
    path('registro/', views.registro, name='registro'),
    path('inicio-sesion/', views.iniciar_sesion, name='inicio_sesion'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('ver-perfil/', views.ver_perfil, name='ver_perfil'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]

