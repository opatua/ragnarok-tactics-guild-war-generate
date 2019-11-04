from django.urls import path
from django.conf.urls import include, url
from duapola_backend import views

urlpatterns = [
    url(
        r'^api/(?P<version>(1))/',
        include(
            [
                path('sign-in', views.SignInView.as_view()),
                path('sign-up', views.SignUpView.as_view()),
            ]
        )
    )
]
