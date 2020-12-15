from django.db.models.query import RawQuerySet
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Board, Topic

# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)         
    return render(request, 'topics.html', {'board': board})

def contact_us(request):
    return render(request, 'contact_us.html')

def about(request):
    return render(request,'about.html')

def profile(request):
    return render(request, 'profile.html')

def trial(request):
    return render(request, 'trial.html')


