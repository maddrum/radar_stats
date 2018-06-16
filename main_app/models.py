from django.db import models


# Create your models here.

class TestModel1(models.Model):
    test = models.CharField(max_length=10)
    test1 = models.IntegerField()
