from django.shortcuts import render
from django.views.generic import TemplateView
from fussion_charts.fusioncharts import FusionCharts
from charts.models import MostPlanesTakeOff, MostPlanesLanded


# Create your views here.
def most_landed_planes(request):
    dataSource = {}
    # setting chart cosmetics
    dataSource['chart'] = {
        "caption": "Top 20 planes (registration) landed at Sofia Airport",
        "paletteColors": "#0075c2",
        "bgColor": "#ffffff",
        "borderAlpha": "20",
        "canvasBorderAlpha": "0",
        "usePlotGradientColor": "0",
        "plotBorderAlpha": "10",
        "showXAxisLine": "1",
        "xAxisLineColor": "#999999",
        "showValues": "0",
        "divlineColor": "#999999",
        "divLineIsDashed": "1",
        "showAlternateHGridColor": "0"
    }

    dataSource['data'] = []
    # The data for the chart should be in an array wherein each element of the array is a JSON object as
    # `label` and `value` keys.
    # Iterate through the data in `Country` model and insert in to the `dataSource['data']` list.

    counter = 0
    for key in MostPlanesLanded.objects.all()[:20]:
        data = {}
        data['label'] = key.aircraft_id_landed.registration
        data['value'] = key.number_of_times_landed
        dataSource['data'].append(data)

    # Create an object for the Column 2D chart using the FusionCharts class constructor
    column2D = FusionCharts("column2D", "ex1", "600", "400", "chart-1", "json", dataSource)
    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.

    return render(request, 'charts/sample.html', {'output': column2D.render()})
