from django.urls import path 
from . import views

urlpatterns = [
    # About Page And Help Page
    path('home/' , views.HOME , name= 'home'),
    path('help/' , views.HELP, name = 'help'),

    # Fonctions 
    path('home/fonctions/youtube/', views.YOUTUBE_FONCTIONS , name = 'youtube'),
    path('home/fonctions/facebook/', views.FACEBOOK_FONCTIONS , name = 'facebook'),
    path('home/fonctions/instagram/', views.INSTAGRAM_FONCTIONS , name = 'instagram'),
    path('home/fonctions/twitch/', views.TWITCH_FONCTIONS , name = 'twitch'),
    
    # Download Page <str:platform>/
    path('home/<str:pk>/download/', views.DOWNLOAD , name ='download'),
    
    
]
