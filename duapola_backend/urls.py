from django.urls import path
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from duapola_backend import views

router = DefaultRouter(trailing_slash=False)
router.register(r'address', views.AddressViewSet, 'address')
router.register(r'category', views.CategoryViewSet, 'category')
router.register(r'city', views.CityViewSet, 'city')
router.register(r'color', views.ColorViewSet, 'color')
router.register(r'country', views.CountryViewSet, 'country')
router.register(r'currency', views.CurrencyViewSet, 'currency')

urlpatterns = [
    url(
        r'^api/(?P<version>(1))/',
        include(
            [
                path('change-password', views.ChangePasswordView.as_view()),
                path('login', views.LoginView.as_view()),
                path('register', views.RegisterView.as_view()),
                url(r'^', include(router.urls)),
            ]
        )
    )
]
