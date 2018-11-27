from django.shortcuts import render
from django.http import HttpResponse

#Test view - Hello World
def index(request):
    return HttpResponse("Hello world! This will be the main page "
        + "of the app.")

