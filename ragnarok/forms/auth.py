from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from ragnarok.models import User


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'}),
        required=True
    )
    password = forms.CharField(
        widget=forms.widgets.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}),
        required=True
    )


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        required=True,  widget=forms.PasswordInput(attrs={'class': 'form-control'}),)
    new_password1 = forms.CharField(
        required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}),)
    new_password2 = forms.CharField(
        required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}),)
