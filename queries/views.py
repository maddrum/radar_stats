from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from queries.forms import QueryData
from database_reader.models import Flights, Aircraft
from django.utils import timezone
from django_countries.data import COUNTRIES


def type_assign_helper(data_dict):
    # helper function which assigns proper data type - int, strings, datetime etc
    result_dict = {}
    for raw_item in data_dict:
        splitter_raw = raw_item.split("__")
        item = splitter_raw[0]
        parameter_type = QueryData.parameters_dict[item]['type']
        if parameter_type == 'int':
            if len(splitter_raw) > 1:
                if splitter_raw[1] == 'range':
                    result_dict[raw_item] = tuple(map(int, (data_dict[raw_item])))
                else:
                    result_dict[raw_item] = int(data_dict[raw_item])
            else:
                result_dict[raw_item] = int(data_dict[raw_item])
        elif parameter_type == 'datetime':
            datetime_format = '%Y-%m-%d %H:%M'
            date_time = timezone.datetime.strptime(data_dict[raw_item], datetime_format)
            if raw_item == 'starttime':
                date_time_item = 'starttime__gte'
            else:
                date_time_item = 'endtime__lte'
            result_dict[date_time_item] = date_time
        elif parameter_type == 'bool':
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
    query_post_data = {key: value for key, value in dict(request.POST).items() if key != "csrfmiddlewaretoken"}
    selectors = {
        'less': 'lt',
        'less or equal': 'lte',
        'equal': 'equal',
        'greater or equal': 'gte',
        'greater': 'gt',
        'between': 'range',
    }
    arguments = {}
    parameters = QueryData.parameters_dict
    for item in query_post_data:
        key = item.split("_")
        form_selector = parameters[key[0]]['selector']
        if form_selector and len(key) == 1:
            selector_key = f'{key[0]}_selector'
            selector = query_post_data[selector_key][0]
            selector_criteria = selectors[selector]
            if selector_criteria != 'equal':
                filter_item = f'{key[0]}__{selector_criteria}'
            else:
                filter_item = key[0]
            arguments[filter_item] = query_post_data[key[0]][0]
            if selector == "between":
                extra_field = f'{key[0]}_extra'
                range_low = query_post_data[item][0]
                range_high = query_post_data[extra_field][0]
                filter_item = f'{item}__range'
                arguments[filter_item] = (range_low, range_high)
        elif len(key) == 1:
            filter_item = f'{item}'
            arguments[filter_item] = query_post_data[item][0]
    # make country with full name form abbreviation
    if 'modescountry' in arguments:
        country_abr = arguments['modescountry']
        country_full_name = COUNTRIES[country_abr]
        arguments['modescountry'] = country_full_name
    aircraft_kwargs = {}
    flight_kwargs = {}
    arguments = type_assign_helper(arguments)
    for item in arguments:
        split_item = item.split("__")[0]
        if parameters[split_item]['table'] == "aircraft":
            # handle changed type field.
            if split_item == 'atype':
                modified_item = 'type__contains'
            else:
                modified_item = item
            key = f'aircraftid__{modified_item}'
            aircraft_kwargs[key] = arguments[item]
        else:
            flight_kwargs[item] = arguments[item]
    print(aircraft_kwargs)
    print(flight_kwargs)
    if aircraft_kwargs:
        result = Flights.objects.select_related().filter(**aircraft_kwargs).exclude(aircraftid__registration='')
        if flight_kwargs:
            result = result.filter(**flight_kwargs)
    else:
        result = Flights.objects.filter(**flight_kwargs).exclude(aircraftid__registration='')
    context_dict = {
        'result': result
    }
    return render(request, 'query/query_results.html', context_dict)
