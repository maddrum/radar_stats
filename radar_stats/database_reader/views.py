from django.shortcuts import render, HttpResponse
from database_reader import models


# Create your views here.
def index(request):
    return render(request, 'index.html')


def aircraft(request):
    aircraft_data = models.Aircraft.objects.exclude(registration='').order_by('country')
    return render(request, 'database_reader/aircraft.html', {'aircraft': aircraft_data})


def flights(request):
    aircraft = models.Flights.objects.all()
    return render(request, 'database_reader/flights.html', {'aircraft': aircraft})
