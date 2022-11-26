from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    products = Product.objects.all()

    
    if request.method == 'POST':
            email_of_newsletter = request.POST['Email']
            send_mail(subject="welcome to newsletter", message='you\'re from now on a member on the newsletter', from_email=settings.EMAIL_HOST_USER, recipient_list=[email_of_newsletter], fail_silently=False)
    context = {
        "products":products,
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


def newsletter(request):
    

    
    return render(request, 'core/contact.html')

