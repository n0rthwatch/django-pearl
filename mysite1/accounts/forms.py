from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User


class RegistrationForm(UserCreationForm):
    name = forms.CharField(required=True, label='Ваше имя и фамилия')
    email = forms.EmailField(required=True, label='Ваш Email-адрес')

    class Meta:
        model = User
        fields = ('name', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    def authenticate_user(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        return user
