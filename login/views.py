# login/views.py
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# Página principal
class IndexView(TemplateView):
    template_name = 'login/index.html'

# Página login necessário
class LoginRequiredView(LoginRequiredMixin, TemplateView):
    template_name = 'login/loginRequired.html'

# Página de registro
class RegisterView(FormView):
    template_name = 'login/register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

# Página de login
class LoginView(FormView):
    template_name = 'login/login.html'
    form_class = CustomAuthenticationForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
        return super().form_invalid(form)
