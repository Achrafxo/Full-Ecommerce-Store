from django.shortcuts import render


def LogPage(request):
    return render(request, 'Authentication/login.html')
