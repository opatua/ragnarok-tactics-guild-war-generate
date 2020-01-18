from django.urls import path

from duapola_admin import views

urlpatterns = [
    # Authentication
    path(
        '',
        views.LoginView.as_view(),
        name='admin_login'
    ),

    # Dashboard
    path(
        'dashboard',
        views.DashboardView.as_view(),
        name='admin_dashboard'
    ),
]
