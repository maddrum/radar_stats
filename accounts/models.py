from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.
class UserQueries(models.Model):
    User = get_user_model()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    query_name = models.CharField(max_length=100)
    query_aircraft_args = models.TextField(blank=True)
    query_flight_args = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('queries:save_query_success')
