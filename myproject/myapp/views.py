from django.shortcuts import render,redirect
from .models import Login,Create_ak,Contact
from .forms import LoginForm,Create_akForm,ContactForm

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = Create_akForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Create_akForm()
    return render(request,'register.html',{'form':form})

def password_reset(request):
    return render(request,'password-reset.html')

def error(request):
    return render(request,'404.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form})