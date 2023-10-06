from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password1",
            "password2"
        ]

    email = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput()
    )

    username = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput()
    )

    password1 = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.PasswordInput()
    )


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username']

    username = forms.CharField(max_length=64, required=True, widget=forms.TextInput())
