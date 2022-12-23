from django.urls import path
from mundial_app import views

urlpatterns = [
    path('equipoCampeon/<int:id>', views.mostrarEquipo),
    path('equipoCampeon', views.mostrarEquipos)
]