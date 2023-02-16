"""
User application forms
"""
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()


class SignInForm(AuthenticationForm):
    username = forms.CharField(max_length=32, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': "password",
        'placeholder': "Password",
    }))


class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Username", max_length=32, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'placeholder': 'Username',
    }))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'placeholder': 'Enter E-Mail'
    }))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': "password",
        'placeholder': "Password",
    }))
    password2 = forms.CharField(label="Confirm_password", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': "confirmPassword",
        'placeholder': "Confirm_password",
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
