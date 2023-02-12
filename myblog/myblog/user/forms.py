"""
User application forms
"""
from  django import forms

class SignInForm(forms.Form):
    username = forms.CharField(label="Username", max_length=32)
    password = forms.CharField(label="Password")


class SignUpForm(forms.Form):
    username = forms.CharField(label="Username", max_length=32)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password")
    confirm_password = forms.CharField(label="Confirm_password")