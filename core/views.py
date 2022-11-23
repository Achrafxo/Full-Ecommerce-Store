from django.shortcuts import render


def home(request):
    return render(request, 'core/index.html')




def Dashboard(request):
    return render(request, 'core/dashboard.html')




def Contact(request):
    return render(request, 'core/contact.html')



def Product_Details(request, pk):
    return render(request, 'core/Product_Details.html')

    