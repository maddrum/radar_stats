# Generated by Django 2.0.2 on 2018-05-24 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_reader', '0003_auto_20180523_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='yearbuilt',
            field=models.IntegerField(blank=True, db_column='YearBuilt', null=True),
        ),
    ]