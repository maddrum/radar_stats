from django.db import models


# Create your models here.
class TestLocalMake(models.Model):
    test = models.CharField(max_length=20)

