from django.shortcuts import render
from django.views.generic import TemplateView
from fussion_charts.fusioncharts import FusionCharts
from charts.models import Stats, MostPlanesTakeOff, MostPlanesLanded, TakeOffDayTimes, LandingsDayTimes


# Create your views here.
def most_landed_takeoff_planes(request):
    context_dict = {}
    # landings
    dataSource = {}
    # setting chart cosmetics
    dataSource['chart'] = {
        "caption": "Top 20 planes take-offs at Sofia Airport",
        "paletteColors": "#af2f2f",
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


    for key in MostPlanesTakeOff.objects.all()[:20]:
        data = {}
        data['label'] = key.aircraft_id_take_off.registration
        data['value'] = key.number_of_take_offs
        dataSource['data'].append(data)

    # Create an object for the Column 2D chart using the FusionCharts class constructor
    column2D_take_off = FusionCharts("column3D", "ex1", "600", "400", "chart-1", "json", dataSource)
    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    context_dict['output_take_off'] = column2D_take_off.render()
    # take off stats
    # landing_stats_query = Stats.objects.get(stats_name='MostPlanesLanded')
    # landing_number = landing_stats_query.records_processed
    # landing_update_time = landing_stats_query.time_last_updated
    # context_dict['landing_number_of_records'] = landing_number
    # context_dict['landing_update_time'] = landing_update_time

    # take-offs
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Top 20 planes landings at Sofia Airport",
        "paletteColors": "#96ba97",
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
    for key in MostPlanesLanded.objects.all()[:20]:
        data = {}
        data['label'] = key.aircraft_id_landed.registration
        data['value'] = key.number_of_times_landed
        dataSource['data'].append(data)
    column2D_landing = FusionCharts("column3D", "ex2", "600", "400", "chart-2", "json", dataSource)
    context_dict['output_landing'] = column2D_landing.render()

    return render(request, 'charts/take-off-landing.html', context_dict)


def hour_take_offs_and_landings(request):
    context_dict = {}
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Take-Offs for day hours",
        "paletteColors": "#af2f2f",
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
        "showAlternateHGridColor": "0",
        "showYAxisLine": "1",
        "numVDivLines": "23",
    }
    dataSource['data'] = []
    for key in TakeOffDayTimes.objects.all():
        data = {}
        data['label'] = str(key.time_of_the_day)
        data['value'] = key.number_of_planes
        dataSource['data'].append(data)

    column2D_take_off = FusionCharts("Line", "ex1", "600", "400", "chart-1", "json", dataSource)
    context_dict['output_take_off'] = column2D_take_off.render()
    # landing stats
    # landing_stats_query = Stats.objects.get(stats_name='MostPlanesLanded')
    # landing_number = landing_stats_query.records_processed
    # landing_update_time = landing_stats_query.time_last_updated
    # context_dict['landing_number_of_records'] = landing_number
    # context_dict['landing_update_time'] = landing_update_time

    # take-offs
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Landings for day hours",
        "paletteColors": "#96ba97",
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
        "showAlternateHGridColor": "0",
        "showYAxisLine": "1",
        "numVDivLines": "23",
    }
    dataSource['data'] = []
    for key in LandingsDayTimes.objects.all():
        data = {}
        data['label'] = str(key.time_of_the_day)
        data['value'] = key.number_of_planes
        dataSource['data'].append(data)
    column2D_landing = FusionCharts("Line", "ex2", "600", "400", "chart-2", "json", dataSource)
    context_dict['output_landing'] = column2D_landing.render()

    return render(request, 'charts/take-off-landing.html', context_dict)
