from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView
import logging

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('feed')
            else:
                return render(request, 'registration/login.html', {'form': form, 'error': 'Invalid username or password'})
        else:
            return render(request, 'registration/login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    print("Usuário deslogado")
    return redirect('index')

'''logger = logging.getLogger(__name__)

def custom_logout_view(request):
    logger.debug("Iniciando processo de logout")
    logout(request)
    logger.debug("Usuário deslogado")
    return redirect('/')'''

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/auto/feed/'
