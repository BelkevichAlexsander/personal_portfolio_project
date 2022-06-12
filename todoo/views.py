from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .forms import TodooForm
from .models import Todoo

 

def singupUser(request):

    if request.method == 'GET':
        return render(request, 'todoo/singupUser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('todoo:currenttodoo')
            except IntegrityError:
                return render(request, 'todoo/singupUser.html', {'form': UserCreationForm(), "error": "This name is busy. Please input another name"  })
        else:
            return render(request, 'todoo/singupUser.html', {'form': UserCreationForm(), "error": "Password don`t match"  })

def loginUser(request):
    if request.method == 'GET':
        return render(request, 'todoo/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todoo/login.html', {'form': AuthenticationForm(), "error": "User name and password  don`t match"})
        else:
            login(request, user)
            return redirect('todoo:currenttodoo')

@login_required
def createtodoo(request):
    if request.method == 'GET':
        return render(request, 'todoo/createtodoo.html', {'form': TodooForm()})
    else:
        try:
            form = TodooForm(request.POST)
            newTodoo = form.save(commit=False)
            newTodoo.user = request.user
            newTodoo.save()
            return redirect('todoo:currenttodoo')
        except ValueError:
            return render(request, 'todoo/createtodoo.html', {'form': TodooForm(), 'error': "Bad data passed in"})

@login_required
def currenttodoo(request):
    todoo = Todoo.objects.filter(user = request.user, datecomplited__isnull = True)
    return render(request, 'todoo/currenttodoo.html', {'todoo': todoo})

@login_required
def logoutUser(request):
    if request.method == "POST":
        logout(request)
        return redirect('todoo:currenttodoo')

@login_required
def viewtodoo(request, todoo_pk):
    todoo = get_object_or_404(Todoo, pk=todoo_pk, user=request.user)
    if request.method == 'GET':
        form = TodooForm(instance=todoo)
        return render(request, 'todoo/viewtodoo.html', {'todoo': todoo, 'form': form})
    else:
        try:
            form = TodooForm(request.POST, instance=todoo)
            form.save()
            return redirect('todoo:currenttodoo')
        except ValueError:
            return render(request, 'todoo/viewtodoo.html', {'todoo': todoo, 'form': form, 'error': 'Bad info input'})

@login_required
def complitetodoo(request, todoo_pk):
    todoo = get_object_or_404(Todoo, pk=todoo_pk, user=request.user)
    if request.method == 'POST':
        todoo.datecomplited = timezone.now()
        todoo.save()
        return redirect('todoo:currenttodoo')

@login_required
def deletetodoo(request, todoo_pk):
    todoo = get_object_or_404(Todoo, pk=todoo_pk, user=request.user)
    if request.method == 'POST':
        todoo.delete()
        return redirect('todoo:currenttodoo')

@login_required
def complitedtodoo(request):
    todoo = Todoo.objects.filter(user = request.user, datecomplited__isnull = False).order_by('-datecomplited')
    return render(request, 'todoo/complitedtodoo.html', {'todoo': todoo})
