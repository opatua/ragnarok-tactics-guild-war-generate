from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from ragnarok.forms import LoginForm
from ragnarok.models import User


class LoginView(FormView):
    template_name = 'account/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(reverse_lazy('guild_war_suggestion'))
        else:
            # messages.success(request, "Invalid Login")
            return HttpResponseRedirect(reverse_lazy('login'))
