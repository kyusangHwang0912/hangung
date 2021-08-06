from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import random
from datetime import datetime


def gyungbokgung(request):
    latitude = request.GET.get('latitude', 37.579634)
    longitude = request.GET.get('longitude', 126.977599)
    contents = {
        'lat': latitude,
        'long': longitude
    }
    return render(request, 'gyungbokgung.html', contents)
