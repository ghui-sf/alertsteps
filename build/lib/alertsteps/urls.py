from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='alertsteps-home'),
    path('about', views.about, name='alertsteps-about'),
]