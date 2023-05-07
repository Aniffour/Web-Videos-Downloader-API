from django.shortcuts import render


# About Page
def HOME(request)  : 
    return render(request,'MAIN/home.html')

# HELP Page 
def HELP(request) : 
    return render( request , 'MAIN/help.html')

# DOWNLOAD PAGE 
def DOWNLOAD(request, pk  ) : 
    return render(request,'DOWNLOAD/download.html')


# FONCTIONS YOUTUBE
def YOUTUBE_FONCTIONS(request) : 
    return render(request, 'FONCTIONS/youtube_fonctions.html')

# FONCTIONS INSTAGRAM
def INSTAGRAM_FONCTIONS(request) : 
    return render(request, 'FONCTIONS/instagram_fonctions.html')

# FONCTIONS FACEBOOK
def FACEBOOK_FONCTIONS(request) : 
    return render(request, 'FONCTIONS/FACEBOOK_fonctions.html')

# FONCTIONS TWITCH
def TWITCH_FONCTIONS(request) : 
    return render(request, 'FONCTIONS/twitch_fonctions.html')