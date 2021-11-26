from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import UserLoginForm,UserRegisterForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username,password=password)
            if user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    context = {
        'title': 'Geekshop | Авторизация',
        'form' : form
    }
    return render(request,'authapp/login.html',context)


def register(request):
    context = {
        'title': 'Geekshop | Регистрация',
    }
    return render(request,'authapp/register.html',context)