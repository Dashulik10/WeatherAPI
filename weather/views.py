from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from WeatherAPI import settings
from weather.models import WeatherData
import requests


class Searcher(TemplateView):
    template_name = 'weather/searcher.html'
    model = WeatherData
    context_object_name = 'searcher'
    weather_data = {}

    def get(self, request, *args, **kwargs):
        city_name = request.GET.get('city_name')
        weather_data = {}

        if city_name:
            url = (f'https://api.openweathermap.org/data/2.5/weather?'
                   f'q={city_name}&units=metric&appid={settings.OPENWEATHER_API_KEY}')
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city_name': city_name,
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'humidity': data['main']['humidity'],
                    'wind_speed': data['wind']['speed'],
                }

                WeatherData.objects.create(city_name=city_name,
                                           temperature=data['main']['temp'],
                                           description=data['weather'][0]['description'],
                                           humidity=data['main']['humidity'],
                                           wind_speed=data['wind']['speed'])

            else:
                weather_data = {'error': 'City not found or API issue!'}

        return render(request, self.template_name, {'weather_data': weather_data})

class HistoryList(ListView):
    model = WeatherData
    template_name = 'weather/history.html'
    context_object_name = 'weather_history'

    def get_queryset(self):
        return WeatherData.objects.all()