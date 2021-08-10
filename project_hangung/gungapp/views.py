from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import random
from datetime import datetime


def gyungbokgung(request):
    gung = request.GET.get('gung', '경복궁')
    latitude = request.GET.get('lat', 37.580001487638526)
    longitude = request.GET.get('long', 126.97694064105475)
    contents = {
        'gung': gung,
        'lat': latitude,
        'long': longitude
    }
    return render(request, 'gyungbokgung.html', contents)


def changdukgung(request):
    gung = request.GET.get('gung', '창덕궁')
    latitude = request.GET.get('lat', 37.57953367677498)
    longitude = request.GET.get('long', 126.99099020142063)
    contents = {
        'gung': gung,
        'lat': latitude,
        'long': longitude
    }
    return render(request, 'changdukgung.html', contents)


def changgyunggung(request):
    gung = request.GET.get('gung', '창경궁')
    latitude = request.GET.get('lat', 37.57904921648744)
    longitude = request.GET.get('long', 126.99485317163106)
    contents = {
        'gung': gung,
        'lat': latitude,
        'long': longitude
    }
    return render(request, 'changgyunggung.html', contents)


def duksugung(request):
    gung = request.GET.get('gung', '덕수궁')
    latitude = request.GET.get('lat', 37.565940338116526)
    longitude = request.GET.get('long', 126.97513498739525)
    contents = {
        'gung': gung,
        'lat': latitude,
        'long': longitude
    }
    return render(request, 'duksugung.html', contents)
