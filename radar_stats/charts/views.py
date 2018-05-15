from django.shortcuts import render
from django.views.generic import TemplateView
from fussion_charts.fusioncharts import FusionCharts
from database_reader.models import Flights


# Create your views here.
def chart(request):
    dataSource = {}
    # setting chart cosmetics
    dataSource['chart'] = {
        "caption": "Top 10 Most Populous Countries",
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
    for key in Flights.objects.select_related().filter(aircraftid__country='')[:10]:
        data = {}
        data['label'] = key.aircraftid.country
        data['value'] = key.flightid
        dataSource['data'].append(data)

        # Create an object for the Column 2D chart using the FusionCharts class constructor
    column2D = FusionCharts("column2D", "ex1", "600", "400", "chart-1", "json", dataSource)
    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.

    return render(request, 'charts/sample.html', {'output': column2D.render()})
