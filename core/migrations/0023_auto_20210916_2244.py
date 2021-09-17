# Generated by Django 3.1.13 on 2021-09-17 01:44

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20210916_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imovel',
            name='id',
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkin_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 22, 44, 12, 805039)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 17, 22, 44, 12, 805091)),
        ),
        migrations.AlterField(
            model_name='hospede',
            name='adultos',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='codigo_imovel',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
