# Generated by Django 2.0.1 on 2018-03-10 02:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistMoneda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField(null=True)),
                ('preciousd', models.FloatField(null=True)),
                ('preciobtc', models.FloatField(null=True)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('symbol', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField(null=True)),
                ('preciousd', models.FloatField(null=True)),
                ('preciobtc', models.FloatField(null=True)),
            ],
        ),
    ]
