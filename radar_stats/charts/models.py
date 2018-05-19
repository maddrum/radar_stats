from django.db import models
from database_reader.models import Flights, Aircraft
from django.utils import timezone


# Create your models here.
def summarize_generator(key_in):
    # create summarize plane data from type Plane_id:number count, for query data passed
    summarize = {}
    counter = 1
    for key in key_in:
        plane_count = 0
        aircraft_pk = key.aircraftid
        if aircraft_pk in summarize:
            plane_count = summarize[aircraft_pk]
        plane_count += 1
        summarize[aircraft_pk] = plane_count
        counter += 1
    return summarize, counter


class Stats(models.Model):
    stats_name = models.CharField(max_length=150)
    records_processed = models.IntegerField()
    time_last_updated = models.DateTimeField()

    @classmethod
    def stats_writer(self, stats_name, stats_records):
        # writes processed records to stats.
        checker = self.objects.filter(stats_name=stats_name)
        if checker:
            query = self.objects.get(stats_name=stats_name)
            query.records_processed = stats_records
            query.time_last_updated = timezone.now()
            query.save()
        else:
            stats_instance = Stats()
            stats_instance.stats_name = stats_name
            stats_instance.records_processed = stats_records
            stats_instance.time_last_updated = timezone.now()
            stats_instance.save()


class MostPlanesLanded(models.Model):
    aircraft_id_landed = models.ForeignKey(Aircraft, on_delete=models.CASCADE, related_name='landed_aircraft')
    number_of_times_landed = models.IntegerField()

    @classmethod
    def table_drop(self):
        self.objects.all().delete()

    @classmethod
    def data_processor(self):
        name_for_stats = __class__.__name__
        self.table_drop()
        query_keys = Flights.objects.filter(lastaltitude__lt=5000)
        summarize, records_counter = summarize_generator(key_in=query_keys)
        # add processed records to statistics
        Stats().stats_writer(stats_name=name_for_stats, stats_records=records_counter)
        id = 0
        bulk_array = []
        for item in sorted(summarize, key=summarize.get, reverse=True)[:100]:
            array_item = MostPlanesLanded(aircraft_id_landed=item, number_of_times_landed=summarize[item], id=id)
            id += 1
            bulk_array.append(array_item)
        self.objects.bulk_create(bulk_array)
        return name_for_stats, records_counter


class MostPlanesTakeOff(models.Model):
    aircraft_id_take_off = models.ForeignKey(Aircraft, on_delete=models.CASCADE, related_name="takeoff_aircraft")
    number_of_take_offs = models.IntegerField()

    @classmethod
    def table_drop(self):
        self.objects.all().delete()

    @classmethod
    def data_processor(self):
        name_for_stats = __class__.__name__
        self.table_drop()
        bulk_array = []
        query_keys = Flights.objects.filter(firstaltitude__lte=5000)
        summarize, records_counter = summarize_generator(key_in=query_keys)
        # add processed records to statistics
        Stats().stats_writer(stats_name=name_for_stats, stats_records=records_counter)
        id = 0
        for item in sorted(summarize, key=summarize.get, reverse=True)[:100]:
            array_item = MostPlanesTakeOff(id=id, aircraft_id_take_off=item, number_of_take_offs=summarize[item])
            id += 1
            bulk_array.append(array_item)
        self.objects.bulk_create(bulk_array)
        return name_for_stats, records_counter
