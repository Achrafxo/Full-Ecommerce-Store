from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *



def LoginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('storepage')
        else:
            messages.warning(request, 'there is an error')
    return render(request, 'Authentication/login.html')



def RegisterPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            messages.success(request, 'Welcome ' + username +'! Your account have been created succesfully.')
            user = authenticate(request, username=username, password=password)
            login(request, user)
    context = {
        'form':form
    }
    return render(request, 'Authentication/register.html', context)


def StorePage(request):
    return render(request, 'Authentication/index.html')


def Logoutfunction(request):
    
    logout(request)
    return redirect('storepage')