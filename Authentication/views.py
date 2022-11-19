from django.shortcuts import render


def LoginPage(request):
    return render(request, 'Authentication/login.html')

def RegisterPage(request):
    return render(request, 'Authentication/register.html')
