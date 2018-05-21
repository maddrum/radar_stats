from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from queries.forms import QueryData
from django.forms.widgets import HiddenInput


# Create your views here.
class QueryEntryStep(TemplateView):
    template_name = 'query/query_start.html'


def query_step_two(request):
    if request.method != 'POST':
        return HttpResponse("No STEP 1 POST data. Please return to <a href = './query-start'> STEP 1</a>.")

    chosen_fields = request.POST.getlist('to')
    print(chosen_fields)
    form = QueryData(chosen_fields=chosen_fields)
    form.order_fields(chosen_fields)
    return render(request, 'query/query-step-two.html', {'form': form})
