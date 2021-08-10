from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import random
from datetime import datetime


def gyungbokgung(request):
    gung = request.GET.get('gung', '경복궁')
    contents = {
        'gung': gung,
    }
    return render(request, 'gyungbokgung.html', contents)


def changdukgung(request):
    gung = request.GET.get('gung', '창덕궁')
    contents = {
        'gung': gung,
    }
    return render(request, 'changdukgung.html', contents)


def changgyunggung(request):
    gung = request.GET.get('gung', '창경궁')
    contents = {
        'gung': gung,
    }
    return render(request, 'changgyunggung.html', contents)


def duksugung(request):
    gung = request.GET.get('gung', '덕수궁')
    contents = {
        'gung': gung,
    }
    return render(request, 'duksugung.html', contents)
