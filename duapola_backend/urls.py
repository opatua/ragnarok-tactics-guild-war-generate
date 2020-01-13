from django.urls import path
from django.conf.urls import include, url
from duapola_backend import views

urlpatterns = [
    url(
        r'^api/(?P<version>(1))/',
        include(
            [
                path('login', views.LoginView.as_view()),
                path('register', views.RegisterView.as_view()),
            ]
        )
    )
]
