from django.urls import path
# from .views import board_topics, contact_us
from django.conf.urls import url
from . import views

# urlpatterns = [
#     path('', home.as_view(), name="home")
# ]
urlpatterns = [
    path('contact_us/', views.contact_us, name='contact_us'),
    # path('board_topics/', views.board_topics, name='board_topics'),
    # path('<int:pk>/', views.board_topics, name= 'board_topics'),
    # path('about_us/', views.about_us, name='about_us'),
    path('about/', views.about, name='about'),
    path('profile/',views.profile, name='profile'),
    path('trial/',views.trial, name='trial')
   
]