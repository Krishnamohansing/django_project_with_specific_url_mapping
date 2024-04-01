from django.urls import path
from mobiles.views import *
app_name='anythings'
urlpatterns = [
    path('oppo/',oppo,name='oppo'),
    path('realme/',realme,name='realme'),
]
