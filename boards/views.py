from django.shortcuts import render
from django.http import HttpResponse
from .models import Board, Topic

# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    # topics = Topic(subject="Jamming", board = "Tee's Blog")
    board = Board.objects.get(pk=pk)
    # topics = Topic.objects.all()
    return render(request, 'topics.html', {'board': board})

def contact_us(request):
    return render(request, 'contact_us.html')

def about(request):
    return render(request,'about.html')

def profile(request):
    return render(request, 'profile.html')

def trial(request):
    return render(request, 'trial.html')


