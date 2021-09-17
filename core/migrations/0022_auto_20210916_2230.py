# Generated by Django 3.1.13 on 2021-09-17 01:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20210916_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='diarias',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='valor',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkin_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 22, 30, 27, 966745)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 17, 22, 30, 27, 966801)),
        ),
        migrations.AlterField(
            model_name='hospede',
            name='adultos',
            field=models.IntegerField(max_length=20),
        ),
    ]
