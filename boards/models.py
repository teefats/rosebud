# from datetime import timedelta
from django.db import models
# from django.db.models.deletion import CASCADE
# from django.db.models.fields import CharField, EmailField, related
# from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse
# from django.utils.text import Truncator

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description= models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject= models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name= 'topics', on_delete=CASCADE)
    starter = models.ForeignKey(User, related_name='topics', on_delete=CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject

class Post(models.Model):
    message= models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=CASCADE)

    def __str__(self):
        return self.message


# class User(models.Model):
#     username= models.CharField(unique=True)
#     password = models.CharField(max_length=20)
#     email = models.EmailField()
#     is_superuser = models.BooleanField()