from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404


# Create your views here.

def anasayfa(request):
    return render(request, "anasayfa.html")

def hakkimizda(request):
    return render(request, "hakkimizda.html")

def cv(request):
    return render(request, 'cv.html')

