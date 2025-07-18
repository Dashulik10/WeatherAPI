# Generated by Django 4.2.5 on 2025-07-14 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100, verbose_name='City Name')),
                ('temperature', models.FloatField(verbose_name='Temperature in Celsius')),
                ('description', models.CharField(max_length=100, verbose_name='Description of Condition')),
                ('humidity', models.IntegerField(verbose_name='Humidity in %')),
                ('wind_speed', models.FloatField(verbose_name='Wind Speed in Km/h')),
                ('time_of_query', models.DateTimeField(auto_now_add=True, verbose_name='Time of Query in UTC')),
            ],
            options={
                'verbose_name': 'Weather Data',
                'verbose_name_plural': 'Weather Data',
                'ordering': ['-time_of_query'],
            },
        ),
    ]
