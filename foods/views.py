from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def chicken(request):
    return render(request,'chicken.html')
def biryani(request):
    return render(request,'biryani.html')
def dbc(request):
    return HttpResponse("<center><h1>Dal Bhat Chokha is one the famous dish of Bihar</h1></center>")