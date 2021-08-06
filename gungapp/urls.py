from django.urls import path
from . import views

urlpatterns = [
    path('gyungbokgung/',views.gyungbokgung, name='gyungbokgung'),
]