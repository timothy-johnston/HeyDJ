
from django.urls import path
from . import views

#Endpoints
urlpatterns = [
    path('', views.index, name='index'),
    
    #Get question info
    path('<int:playlist_id>/', views.getPLInfo, name='plinfo')

]