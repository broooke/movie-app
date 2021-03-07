import random

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect


# Create your views here.
from authorization.forms import UserRegisterForm


def loginUser(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list-movies')
            else:
                messages.info(request, 'Password or Username is incorrect')

    context = {'form': form}
    return render(request, 'page/login.html', context)

def signupUser(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            code = generateCode()
            request.session['code'] = code
            email = form.cleaned_data['email']
            request.session['email'] = email
            password = form.cleaned_data['password1']
            user = authenticate(username=email, password=password)
            send_mail('код подтверждения', code,
                      settings.EMAIL_HOST_USER,
                      [email],
                      fail_silently=False)
            if user and user.is_active:
                login(request,user)
                return redirect('list-movies')
            else:
                return redirect('register-confirm')
    context = {'form':form}
    return render(request, 'page/login.html', context)

def generateCode():
    random.seed()
    return str(random.randint(10000, 99999))

def confirmSignUp(request):
    if request.method == 'POST':
        code = request.POST['code']
        if code == request.session['code']:
            user = User.objects.get(username=request.session['email'])
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('list-movies')
        else:
            messages.add_message(request, messages.INFO, 'Code incorrect')
            return render(request, 'page/signupConfirm.html')
    return render(request, 'page/signupConfirm.html')

def logoutUser(request):
    logout(request)
    return redirect('home')
