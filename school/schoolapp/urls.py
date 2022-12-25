from django.urls import include
from django.urls import re_path as url
from django.urls import path, reverse
from .views import Index,NewsView, PhotoView
from django.shortcuts import render

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('students/', lambda request: render(request, 'schoolapp/students.html'), name='students'),
    path('news/', NewsView.as_view(), name='news'),
    path('map/', lambda request: render(request, 'schoolapp/map.html'), name='map'),
    path('family/', lambda request: render(request, 'schoolapp/family.html'), name='family'),
    path('information/', lambda request: render(request, 'schoolapp/information.html'), name='information'),
    path('mcs/', lambda request: render(request, 'schoolapp/mcs.html'), name='mcs'),
    path('photo_album/', PhotoView.as_view(), name='photo_album'),
    path('schedule/', lambda request: render(request, 'schoolapp/schedule.html'), name='schedule'),
    path('students/', lambda request: render(request, 'schoolapp/students.html'), name='students'),

]
