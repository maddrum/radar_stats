from django.conf.urls import url
from queries import views

app_name = 'queries'

urlpatterns = [
    url(r'query-start', views.QueryEntryStep.as_view(), name='query_start'),
    url(r'query-step-two', views.query_step_two, name='step_2'),
    url(r'query-result', views.query_results, name='query_result'),
    url(r'query-save$', views.SaveUserQueryCreateView.as_view(), name='save_query'),
    url(r'query-save-success$', views.SaveSuccessView.as_view(), name='save_query_success'),
]
