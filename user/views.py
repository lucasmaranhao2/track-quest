from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import RegisterForm
# Create your views here.

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('user:login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form':form})

def index_view(request):
    return render(request, 'user.html')