# Generated by Django 3.1.13 on 2021-09-16 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210915_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='telefone',
            field=models.BigIntegerField(),
        ),
    ]