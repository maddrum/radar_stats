from django.db import models


# Create your models here.
class OtherTestModel(models.Model):
    test_other = models.CharField(max_length=150)
