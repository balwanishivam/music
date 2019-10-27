from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from .models import *


def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context ={
        'all_albums': all_albums,
    }

    return HttpResponse(templates ,render(context,request))

def details(request ,album_id):
    return HttpResponse("Album Request=>" + str(album_id) )
# Create your views here.
