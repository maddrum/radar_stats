from django.db import models
from database_reader.models import Flights, Aircraft


# Create your models here.
class Stats(models.Model):
    stats_name = models.CharField(max_length=150)
    records_processed = models.IntegerField()


class MostPlanesLanded(models.Model):
    aircraft_id_landed = models.ForeignKey(Aircraft, on_delete=models.CASCADE, related_name='landed_aircraft')
    number_of_times_landed = models.IntegerField()

    @classmethod
    def table_drop(self):
        self.objects.all().delete()

    @classmethod
    def data_processor(self):
        self.table_drop()
        summarize = {}
        counter = 0
        for key in Flights.objects.filter(lastaltitude__lt=5000):
            counter += 1
            plane_count = 0
            aircraft_pk = key.aircraftid
            if aircraft_pk in summarize:
                plane_count = summarize[aircraft_pk]
            plane_count += 1
            summarize[aircraft_pk] = plane_count
        counter = 0
        bulk_array = []
        for item in sorted(summarize, key=summarize.get, reverse=True)[:100]:
            array_item = MostPlanesLanded(aircraft_id_landed=item, number_of_times_landed=summarize[item], id=counter)
            counter += 1
            bulk_array.append(array_item)
        self.objects.bulk_create(bulk_array)


class MostPlanesTakeOff(models.Model):
    aircraft_id_take_off = models.ForeignKey(Aircraft, on_delete=models.CASCADE, related_name="takeoff_aircraft")
    number_of_take_offs = models.IntegerField()

    @classmethod
    def table_drop(self):
        self.objects.all().delete()

    @classmethod
    def data_processor(self):
        self.table_drop()
        summarize = {}
        counter = 0
        for key in Flights.objects.filter(firstaltitude__lte=5000):
            counter += 1
            plane_count = 0
            aircraft_pk = key.aircraftid
            if aircraft_pk in summarize:
                plane_count = summarize[aircraft_pk]
            plane_count += 1
            summarize[aircraft_pk] = plane_count
        counter = 0
        bulk_array = []
        for item in sorted(summarize, key=summarize.get, reverse=True)[:100]:
            array_item = MostPlanesTakeOff(id=counter, aircraft_id_take_off=item, number_of_take_offs=summarize[item])
            counter += 1
            bulk_array.append(array_item)
        self.objects.bulk_create(bulk_array)
