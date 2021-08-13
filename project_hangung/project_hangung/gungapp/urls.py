from django.urls import path
from . import views

urlpatterns = [
    path('gyungbokgung/',views.gyungbokgung, name='gyungbokgung'),
    path('changdukgung/', views.changdukgung, name='changdukgung'),
    path('changgyunggung/', views.changgyunggung, name='changgyunggung'),
    path('duksugung/', views.duksugung, name='duksugung'),
]