from django.urls import path
from duapola_backend.views import auth

urlpatterns = [
    path('auth/login', auth.LoginView.as_view()),
    path('auth/register', auth.RegisterView.as_view()),
]
