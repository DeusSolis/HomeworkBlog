from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from .forms import SignInForm, SignUpForm


def signin_view(request: HttpRequest):
    """User sign in view"""
    if request.method == "POST":
        form = SignInForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            redirect_url = reverse_lazy("list")

            return HttpResponseRedirect(redirect_url)

    form = SignInForm()
    return render(request, 'signin.html', {'form': form})


def signup_view(request: HttpRequest):
    """User sign up view"""
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            redirect_url = reverse_lazy("signin")

            return HttpResponseRedirect(redirect_url)

    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request: HttpRequest):
    logout(request)
    redirect_url = reverse_lazy('list')
    return HttpResponseRedirect(redirect_url)
