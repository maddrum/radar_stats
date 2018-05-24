from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from queries.forms import QueryData
from database_reader.models import Flights, Aircraft
from django.utils import timezone


# Create your views here.
def type_assign_helper(data_dict, parameter):
    result_dict = {}
    for raw_item in data_dict:
        splitter_raw = raw_item.split("__")
        item = splitter_raw[0]
        if parameter[item]['type'] == 'int':
            try:
                if splitter_raw[1] == 'range':
                    result_dict[raw_item] = tuple(map(int, (data_dict[raw_item])))
            except IndexError:
                result_dict[raw_item] = int(data_dict[raw_item])
        elif parameter[item]['type'] == 'datetime':
            datetime_format = '%Y-%m-%d %H:%M:%S'
            date_time = timezone.datetime.strptime(data_dict[raw_item], datetime_format)
            if raw_item == 'starttime':
                date_time_item = 'starttime__gte'
            else:
                date_time_item = 'endtime__lte'
            result_dict[date_time_item] = date_time
        elif parameter[item]['type'] == 'bool':
            if data_dict[raw_item] == 'on':
                result_dict[raw_item] = 1
            else:
                result_dict[raw_item] = 1
        else:
            result_dict[raw_item] = data_dict[raw_item]

    return result_dict


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
    arguments = type_assign_helper(arguments, parameters)

    for item in arguments:
        splitted_item = item.split("__")[0]
        if parameters[splitted_item]['table'] == "aircraft":
            key = f'aircraftid__{item}'
            aircraft_kwargs[key] = arguments[item]
        else:
            flight_kwargs[item] = arguments[item]


    print(aircraft_kwargs)
    print(flight_kwargs)

    if aircraft_kwargs:
        result = Flights.objects.select_related().filter(**aircraft_kwargs)
        if flight_kwargs:
            result.filter(**flight_kwargs)
    else:
        result = Flights.objects.filter(**flight_kwargs)
    context_dict = {
        'result': result}
    return render(request, 'query/query_results.html', context_dict)
