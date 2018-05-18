from django.conf.urls import url
from database_data_processor import views

app_name = 'database_processor'

urlpatterns = [
    url(r'proceed-landings', views.landed_planes_generator, name='proceed_landings'),
    url(r'proceed-take-offs', views.take_off_plane_generator, name='proceed_take_offs'),
]
