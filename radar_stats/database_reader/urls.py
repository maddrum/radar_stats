from django.urls import re_path
from database_reader import views

app_name = 'database_reader'

urlpatterns = [
    re_path(r'aircraft/', views.aircraft, name="aircraft"),
    re_path(r'flights/', views.flights, name='flights')
]
