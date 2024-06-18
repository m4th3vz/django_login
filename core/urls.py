from django.urls import path  # Importa a função path do módulo django.urls
from . import views  # Importa as views definidas no diretório views.py
from django.contrib.auth import views as auth_views  # Importa as views de autenticação do Django com um alias 'auth_views'

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),  # Define a URL raiz como a view 'index' com o nome 'index'
    # Página login necessário
    path('loginRequired/', views.loginRequired, name='loginRequired'),  # Define a URL '/loginRequired/' como a view 'loginRequired' com o nome 'loginRequired'
    # Página de registro
    path('register/', views.register_view, name='register'),  # Define a URL '/register/' como a view 'register_view' com o nome 'register'
    # Página de login
    path('login/', views.login_view, name='login'),  # Define a URL '/login/' como a view 'login_view' com o nome 'login'
    # Página de logout
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),  # Define a URL '/logout/' como a view de logout padrão do Django, redirecionando para 'index' após logout, com o nome 'logout'
]
