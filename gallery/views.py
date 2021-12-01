from django.shortcuts import render
from django.http  import HttpResponse
from .models import photos



def index(request):
    photo = photos.objects.all()
    return render(request,'all-art/index.html',{'photo':photo}) 



