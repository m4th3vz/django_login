# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required

# Página principal
def index(request):
    return render(request, 'core/index.html')

# Página login necessário
@login_required
def loginRequired(request):
    return render(request, 'core/loginRequired.html')

# Página de registro
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Corrigido para redirecionar para 'index'
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})

# Página de login
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Corrigido para redirecionar para 'index'
    else:
        form = CustomAuthenticationForm() 
    return render(request, 'core/login.html', {'form': form})
