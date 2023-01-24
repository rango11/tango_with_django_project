from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<a href = '/rango/about'>Rango says hey there partner!</a>")

def about(request):
    return HttpResponse("<a href = '/'>Rango says here is the about page</a>")



