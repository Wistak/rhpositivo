from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('prospectos', views.prospectos, name='prospectos'),
    path('nuevo_prospecto', views.nuevoProspecto, name='nuevo_prospecto'),
    path('evaluar_prospecto/<str:pk>/', views.evaluarProspecto, name="evaluar_prospecto"),
]