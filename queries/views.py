from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from queries.forms import QueryData
from database_reader.models import Flights,Aircraft


# Create your views here.
class QueryEntryStep(TemplateView):
    template_name = 'query/query_start.html'


def query_step_two(request):
    if request.method != 'POST':
        return HttpResponse("No STEP 1 POST data. Please return to <a href = './query-start'> STEP 1</a>.")

    chosen_fields = request.POST.getlist('to')
    form = QueryData(chosen_fields=chosen_fields)
    form.order_fields(chosen_fields)
    return render(request, 'query/query-step-two.html', {'form': form})


def query_results(request):
    if request.method != 'POST':
        return HttpResponse("No STEP 1 POST data. Please return to <a href = './query-start'> STEP 1</a>.")
    query_post_data = dict(request.POST)
    kwargs = {}
    for item in query_post_data:
        if item != 'csrfmiddlewaretoken':
            filter_item = f'aircraftid__{item}__exact'
            kwargs[filter_item] = query_post_data[item][0]
    print(kwargs)
    result = Flights.objects.select_related().filter(**kwargs)
    for item in result:
        print(item.aircraftid.country)
    context_dict = {
        'result':result
    }
    return render(request, 'query/query_results.html', context_dict)
