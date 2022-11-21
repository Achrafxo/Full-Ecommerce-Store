from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginPage, name='login'),
    path('register', views.RegisterPage, name='register'),
    path('store', views.StorePage, name='storepage'),
    path('logout', views.Logoutfunction, name='logout')
]