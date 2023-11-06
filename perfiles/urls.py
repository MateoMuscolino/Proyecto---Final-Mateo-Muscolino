from django.urls import path
from . import views

urlpatterns = [
    path('', views.mi_pagina, name='mi_pagina'),
    path('registro/', views.registro, name='registro'),
    path('inicio-sesion/', views.iniciar_sesion, name='inicio_sesion'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
]
