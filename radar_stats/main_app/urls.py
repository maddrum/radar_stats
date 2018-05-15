from django.conf.urls import url
from main_app import views

app_name = 'main_app'
urlpatterns = [
    url(r'about/', views.AboutPage.as_view(), name='about'),
]
