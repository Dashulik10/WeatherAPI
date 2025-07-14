from django.urls import path
from weather.views import Searcher, HistoryList

app_name = 'weather'
urlpatterns = [
    path('', Searcher.as_view(), name='searcher'),
    path('history/', HistoryList.as_view(), name='history'),
]