from django.urls import path
from . import views

urlpatterns = [
    path('opiniones/', views.opiniones, name='opiniones'),
    path('agregar-opinion/', views.agregar_opinion, name='agregar_opinion'),
    path('editar-opinion/<int:opinion_id>/', views.editar_opinion, name='editar_opinion'),
    path('eliminar-opinion/<int:opinion_id>/', views.eliminar_opinion, name='eliminar_opinion'),
    path('tus-opiniones/', views.tus_opiniones, name='tus_opiniones'),
]
