from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('user:login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user:index')
        else:
            form = LoginForm(request.POST)
            messages.error(request, 'incorrect username or password. Try again.')
            return render(request, 'login.html', {'form':form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

@login_required
def index_view(request):
    return render(request, 'user.html')