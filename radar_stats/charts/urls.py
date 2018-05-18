from django.conf.urls import url
from charts import views

app_name = 'charts'

urlpatterns = [
    url(r'most-landed-plane', views.most_landed_planes)

]
