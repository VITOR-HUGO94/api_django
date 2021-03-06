# Generated by Django 3.1.13 on 2021-09-15 01:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210913_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saida', models.DateTimeField()),
            ],
        ),
        migrations.RenameField(
            model_name='checkin',
            old_name='diarias',
            new_name='diarias_reservadas',
        ),
        migrations.AddField(
            model_name='checkin',
            name='criado',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='limpeza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_da_limpeza', models.TimeField()),
                ('checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.checkout')),
            ],
        ),
        migrations.AddField(
            model_name='checkout',
            name='checkin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.checkin'),
        ),
    ]
