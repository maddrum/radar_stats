from django.contrib import admin
from charts.models import MostPlanesLanded, MostPlanesTakeOff

# Register your models here.
admin.site.register(MostPlanesLanded)
admin.site.register(MostPlanesTakeOff)
