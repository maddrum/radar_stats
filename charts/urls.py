from django.conf.urls import url
from charts import views

app_name = 'charts'

urlpatterns = [
    url(r'take-offs-and-landings/', views.most_landed_takeoff_planes, name='take-off_landing'),
    url(r'hourly/', views.hour_take_offs_and_landings, name='hour_take_offs_and_landings'),
]
