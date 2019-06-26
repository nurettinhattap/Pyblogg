from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('ab', views.ab),
    path('content', views.content),
    path('new', views.new)
]

