from django.urls import path
from .views import index,login,register,password_reset,error,contact

urlpatterns = [
    path('',index,name='index'),
    path('contact',contact,name='contact'),
    path('login',login,name='login'),
    path('register',register,name='register'),
    path('password_reset',password_reset,name='password_reset'),
    path('error',error,name='error'),
]