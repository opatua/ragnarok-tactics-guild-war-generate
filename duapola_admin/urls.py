from django.urls import path

from duapola_admin import views

urlpatterns = [
    # Authentication
    path('', views.LoginView.as_view(), name='admin_login'),

    # Category URLs
    path('category/data',views.CategoryDataView.as_view(), name='category_data'),
    path('category', views.CategoryListView.as_view(), name='category_index'),
    path('category/create', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/<slug:pk>/update', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/<slug:pk>/delete', views.CategoryDeleteView.as_view(), name='category_delete'),

    # Product Family URLs
    path('product-family/data',views.ProductFamilyDataView.as_view(), name='product_family_data'),
    path('product-family', views.ProductFamilyListView.as_view(), name='product_family_index'),
    path('product-family/create', views.ProductFamilyCreateView.as_view(), name='product_family_create'),
    path('product-family/<slug:pk>/update', views.ProductFamilyUpdateView.as_view(), name='product_family_update'),
    path('product-family/<slug:pk>/delete', views.ProductFamilyDeleteView.as_view(), name='product_family_delete'),

    # Dashboard
    path('dashboard', views.DashboardView.as_view(), name='admin_dashboard'),

    # User URLs
    path('user/data', views.user.UserDataView.as_view(), name='user_data'),
    path('user', views.user.UserListView.as_view(), name='user_index'),
    path('user/create', views.user.UserCreateView.as_view(), name='user_create'),
    path('user/<slug:pk>/update', views.user.UserUpdateView.as_view(), name='user_update'),
    path('user/<slug:pk>/password', views.user.UserPasswordChangeView.as_view(), name='user_password'),
    path('user/<slug:pk>/delete', views.user.UserDeleteView.as_view(), name='user_delete'),
]
