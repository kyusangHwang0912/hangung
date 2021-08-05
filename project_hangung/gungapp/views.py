from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import random
from datetime import datetime


def gyungbokgung(request):
    return render(request, 'gyungbokgung.html')