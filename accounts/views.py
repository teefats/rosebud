
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect, render
from .forms import SignUpForm
# from django.db import models
# from django.contrib.auth.models import User
# from PIL import Image
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            # messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



