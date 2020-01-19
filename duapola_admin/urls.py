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

    # User URLs
    path(
        'user/data',
        views.user.UserDataView.as_view(),
        name='user_data'
    ),
    path(
        'user',
        views.user.UserListView.as_view(),
        name='user_index'
    ),
    path(
        'user/create',
        views.user.UserCreateView.as_view(),
        name='user_create'
    ),
    path(
        'user/<slug:pk>/update',
        views.user.UserUpdateView.as_view(),
        name='user_update'
    ),
    path(
        'user/<slug:pk>/password',
        views.user.UserPasswordChangeView.as_view(),
        name='user_password'
    ),
    path(
        'user/<slug:pk>/delete',
        views.user.UserDeleteView.as_view(),
        name='user_delete'
    ),
]
