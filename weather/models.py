from django.db import models

class WeatherData(models.Model):
    city_name = models.CharField(max_length=100, verbose_name='City Name')
    temperature = models.FloatField(verbose_name='Temperature in Celsius')
    description = models.CharField(max_length=100, verbose_name='Description of Condition')
    humidity = models.IntegerField(verbose_name='Humidity in %')
    wind_speed = models.FloatField(verbose_name='Wind Speed in Km/h')
    time_of_query = models.DateTimeField(auto_now_add=True, verbose_name='Time of Query in UTC')

    class Meta:
        verbose_name = 'Weather Data'
        verbose_name_plural = 'Weather Data'
        ordering = ['-time_of_query']

