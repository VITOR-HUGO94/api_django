# Generated by Django 3.1.13 on 2021-09-13 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='checkin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('nhospedes', models.IntegerField()),
                ('npets', models.IntegerField()),
                ('data', models.DateField(auto_now_add=True)),
                ('diarias', models.IntegerField()),
                ('preço', models.FloatField()),
                ('endereço', models.CharField(max_length=255)),
                ('cod_reserva', models.CharField(max_length=255)),
                ('telefone', models.IntegerField()),
                ('informações', models.CharField(max_length=255)),
            ],
        ),
    ]
