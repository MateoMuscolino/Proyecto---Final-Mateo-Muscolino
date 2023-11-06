from django.urls import path
from . import views

urlpatterns = [
    path('opiniones/', views.opiniones, name='opiniones'),
    path('agregar-opinion/', views.agregar_opinion, name='agregar_opinion'),
]
