from django.urls import path
from . import views

#Endpoints?
urlpatterns = [
    path('', views.index, name='index'),
]