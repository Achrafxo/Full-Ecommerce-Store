from django.shortcuts import render
from .models import *

def home(request):
    products = Product.objects.all()

    context = {
        "products":products
    }
    return render(request, 'core/index.html', context)




def Dashboard(request):
    return render(request, 'core/dashboard.html')




def Contact(request):
    return render(request, 'core/contact.html')



def Product_Details(request, pk):
    product = Product.objects.get(id=pk)

    context = {
        "product":product
    }
    return render(request, 'core/Product_Details.html', context)

    