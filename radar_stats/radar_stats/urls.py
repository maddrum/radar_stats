"""radar_stats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.conf.urls import url
from main_app import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'main/', include('main_app.urls')),
    url(r'database-raw', include('database_reader.urls', namespace='database-raw')),
    url('account/', include('accounts.urls', namespace='accounts')),
    url(r'charts/', include('charts.urls', namespace='charts')),
    url(r'include/', include('queries.urls', namespace='queries')),
    url('admin/', admin.site.urls),

]
