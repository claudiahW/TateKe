from django.shortcuts import render
from django.http  import HttpResponse
from .models import photos

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def index(request):
    return render(request, 'index.html')

def index(request):
    # imports photos and save it in database
    photo = photos.objects.all()
    # adding context 
    ctx = {'photo':photo}
    return render(request, 'index.html', ctx)