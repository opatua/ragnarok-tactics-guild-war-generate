from django.urls import path

from ragnarok import views

urlpatterns = [
    # Authentication
    path('', views.LoginView.as_view(), name='login'),

    # Country URLs
    path('country/data', views.CountryDataView.as_view(), name='country_data'),
    path('country', views.CountryListView.as_view(), name='country_index'),
    path('country/create', views.CountryCreateView.as_view(), name='country_create'),
    path('country/<slug:pk>/update',
         views.CountryUpdateView.as_view(), name='country_update'),
    path('country/<slug:pk>/delete',
         views.CountryDeleteView.as_view(), name='country_delete'),

    # Dashboard
    path('dashboard', views.DashboardView.as_view(), name='admin_dashboard'),
    path('logout', views.LogoutView.as_view(), name='logout'),

    # User URLs
    path('user/data', views.user.UserDataView.as_view(), name='user_data'),
    path('user', views.user.UserListView.as_view(), name='user_index'),
    path('user/create', views.user.UserCreateView.as_view(), name='user_create'),
    path('user/<slug:pk>/update',
         views.user.UserUpdateView.as_view(), name='user_update'),
    path('user/<slug:pk>/password',
         views.user.UserPasswordChangeView.as_view(), name='user_password'),
    path('user/<slug:pk>/delete',
         views.user.UserDeleteView.as_view(), name='user_delete'),
]
