from django.urls import path
from django.urls.resolvers import path 
from . import views

urlpatterns = [
    path('', views.index)
]