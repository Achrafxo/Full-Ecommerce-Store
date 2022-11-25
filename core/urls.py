from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('dashboard/',views.Dashboard, name='dashboard'),
    path('contact/',views.Contact, name='contact'),
    path('details/<str:pk>/', views.Product_Details, name='product details'),
]