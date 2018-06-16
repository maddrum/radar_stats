from django.db import models


# Create your models here.
class NewerTest(models.Model):
    test_char = models.CharField(max_length=50)
