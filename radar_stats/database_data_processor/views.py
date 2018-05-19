from django.shortcuts import render
from charts.models import MostPlanesLanded, MostPlanesTakeOff


# Create your views here.
def landed_planes_generator(request):
    name, records_counter = MostPlanesLanded().data_processor()
    context_dict = {
        'database': name,
        'records_counter': records_counter,
    }

    return render(request, 'database_processor/run_process.html', context_dict)


def take_off_plane_generator(request):
    name, records_counter = MostPlanesTakeOff().data_processor()

    context_dict = {
        'database': name,
        'records_counter': records_counter,
    }

    return render(request, 'database_processor/run_process.html', context_dict)
