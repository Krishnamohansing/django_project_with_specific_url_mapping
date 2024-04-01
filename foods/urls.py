from django.urls import path
from foods.views import *
app_name='Somthing'
urlpatterns = [
    path('chicken/',chicken,name='chicken'),
    path('biryani/',biryani,name='biryani'),
    path('dbc/',dbc,name='dbc'),
]
