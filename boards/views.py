from django.contrib.auth.models import User
from django.db.models.query import RawQuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Board, Topic, Post

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

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    
    if request.method == 'POST':
        subject = request.POST['subject']
        message =request.POST['message']

        user = User.objects.first()

        topic = Topic.objects.create(
            subject = subject,
            board = board,
            starter = user
        )

        post = Post.objects.create(
            message = message,
            topic = topic,
            created_by=user
        )
        return redirect('board_topics', pk=board.pk)
    return render(request, 'new_topic.html', {'board':board})


