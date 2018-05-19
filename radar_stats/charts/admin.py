from django.contrib import admin
from charts.models import Stats, MostPlanesLanded, MostPlanesTakeOff

# Register your models here.
admin.site.register(MostPlanesLanded)
admin.site.register(MostPlanesTakeOff)
admin.site.register(Stats)
