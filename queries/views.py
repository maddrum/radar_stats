from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from queries.forms import QueryData
from database_reader.models import Flights, Aircraft


# Create your views here.
class QueryEntryStep(TemplateView):
    template_name = 'query/query_start.html'


def query_step_two(request):
    if request.method != 'POST':
        return HttpResponse("No STEP 1 POST data. Please return to <a href = './query-start'> STEP 1</a>.")

    chosen_fields = request.POST.getlist('to')
    form = QueryData(chosen_fields=chosen_fields)
    form.order_fields(chosen_fields)
    context_dict = {
        'form': form,
        'parameters': form.parameters_dict
    }
    return render(request, 'query/query-step-two.html', context_dict)


def query_results(request):
    if request.method != 'POST':
        return HttpResponse("No STEP 1 POST data. Please return to <a href = './query-start'> STEP 1</a>.")
    query_post_data = dict(request.POST)
    arguments = {}
    parameters = QueryData.parameters_dict
    for item in query_post_data:
        if item != 'csrfmiddlewaretoken' and len(item.split("_")) == 1:
            if parameters[item]['selector']:
                selector_key = f'{item}_selector'
                selector = query_post_data[selector_key][0]
                if selector == "less":
                    filter_item = f'{item}__lt'
                    arguments[filter_item] = query_post_data[item][0]
                elif selector == "less or equal":
                    filter_item = f'{item}__lte'
                    arguments[filter_item] = query_post_data[item][0]
                elif selector == "equal":
                    filter_item = f'{item}'
                    arguments[filter_item] = query_post_data[item][0]
                elif selector == "greater or equal":
                    filter_item = f'{item}__gte'
                    arguments[filter_item] = query_post_data[item][0]
                elif selector == "greater":
                    filter_item = f'{item}__gt'
                    arguments[filter_item] = query_post_data[item][0]
                elif selector == "between":
                    extra_field = f'{item}_extra'
                    range_low = query_post_data[item][0]
                    range_high = query_post_data[extra_field][0]
                    filter_item = f'{item}__range'
                    arguments[filter_item] = (range_low, range_high)
            else:
                filter_item = f'{item}'
                arguments[filter_item] = query_post_data[item][0]
    aircraft_kwargs = {}
    flight_kwargs = {}
    for item in arguments:
        splitted_item = item.split("__")[0]
        if parameters[splitted_item]['table'] == "aircraft":
            key = f'aircraftid__{item}'
            aircraft_kwargs[key] = arguments[item]
        else:
            flight_kwargs[item] = arguments[item]
    if aircraft_kwargs:
        result = Flights.objects.select_related().filter(**aircraft_kwargs)
        if flight_kwargs:
            result.filter(**flight_kwargs)
    else:
        result = Flights.objects.filter(**flight_kwargs)
    print(aircraft_kwargs)
    print(flight_kwargs)

    context_dict = {
        'result': result
    }

    return render(request, 'query/query_results.html', context_dict)
