from django.shortcuts import render
from django.http import HttpResponse
from .models import Playlist

#Test view - Hello World
def index(request):
    return HttpResponse("Hello world! This will be the main page "
        + "of the app.")

#Test view - Retrieve playlist info baseSd on id (GET)
def getPLInfo(request, playlist_id):
        allPlaylists = Playlist.objects.all()   #Can ignore this error for now, still works...
        plNames = ', '.join([p.pl_name for p in allPlaylists])
        return HttpResponse("Playlist info: %s." % plNames)

#Test view - Augment playlist plays (POST or PUT?)
def changePLPlays(request, playlist_id):
        return HttpResponse("Changing plays for playlist %s." % playlist_id)

