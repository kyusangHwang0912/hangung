from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import random
from datetime import datetime


def gyungbokgung(request):
    gung = request.GET.get('gung', '경복궁')
    latitude = request.GET.get('lat', 37.579634)
    longitude = request.GET.get('long', 126.977599)
    contents = {
        'gung': gung,
        'lat': latitude,
        'long': longitude
    }
    return render(request, 'gyungbokgung.html', contents)
