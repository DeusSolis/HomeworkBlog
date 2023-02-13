from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from .forms import SignInForm, SignUpForm


def signin_view(request: HttpRequest) -> HttpResponse:
    """User sign in view"""
    if request == "POST":
        form = SignInForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            redirect_url = reverse_lazy("list")

            return HttpResponseRedirect(redirect_url)
        form = SignInForm()
        return render(request, "signin.html", {"form": form})

    form = SignInForm()
    return render(request, 'signin.html', {'form': form})


def signup_view(request: HttpRequest) -> HttpResponse:
    """User sign up view"""
    if request == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            redirect_url = reverse_lazy("signup")

            return HttpResponseRedirect(redirect_url)
        redirect_url = reverse_lazy("signup")
        return HttpResponseRedirect(redirect_url)
    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def profile_view(request: HttpRequest) -> HttpResponse:
    """User profile view"""
    return render(request, 'profile.html')


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    redirect_url = reverse_lazy('list')
    return HttpResponseRedirect(redirect_url)
