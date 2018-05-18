from django.shortcuts import render
from charts.models import MostPlanesLanded, MostPlanesTakeOff


# Create your views here.
def landed_planes_generator(request):
    MostPlanesLanded().data_processor()
    return render(request, 'database_processor/run_process.html', {'database': 'Landing'})


def take_off_plane_generator(request):
    MostPlanesTakeOff().data_processor()
    return render(request, 'database_processor/run_process.html', {'database': 'Take-Off '})
