from django.db import models


# Create your models here.
class TestMig(models.Model):
    test111 = models.CharField(max_length=50)
