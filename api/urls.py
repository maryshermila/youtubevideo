from django.contrib import admin
from django.urls import path
from api.views import *
urlpatterns = [
    path('youtubedata',GetYoutubeData.as_view(),name='youtubedata')
]
