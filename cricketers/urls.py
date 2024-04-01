from django.urls import path
from cricketers.views import *
app_name='anything'
urlpatterns = [
    path('thala/',thala,name='thala'),
    path('Hitman/',Hitman,name='Hitman'),
]
