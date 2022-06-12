from django.shortcuts import render
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def information(request):
    return render(request, 'generator/info.html')

def password(request):
    
    characters = list("abcdefghijklmnopqrstuvwxyz")

    if request.GET.get('uppercase'):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get('special'):
        characters.extend(list("!@#$%^&*()_+=-")) 
    if request.GET.get('numbers'):
        characters.extend(list("1234567890"))    

    length = int(request.GET.get('length', 10))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {"password": thepassword})

