from django.conf.urls import url
from queries import views

app_name = 'queries'

urlpatterns = [
    url(r'query-start', views.QueryEntryStep.as_view(), name='query_start'),
    url(r'query-step-two', views.query_step_two, name='step_2'),
]
