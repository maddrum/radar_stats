from django.conf.urls import url
from queries import views

app_name = 'queries'

urlpatterns = [
    url(r'sample', views.sample)
]
