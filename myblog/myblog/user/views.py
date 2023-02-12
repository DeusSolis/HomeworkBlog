from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .forms import SignInForm, SignUpForm
from .models import UserModel


def signin_view(request: HttpRequest) -> HttpResponse:
    """User sign in view"""
    if request == "POST":
        form = SignInForm(request.POST)
    else:
        form = SignInForm()

    return render(request, 'signin.html', {'form': form})
    # if request.method == "POST":
    #     username = request.POST['username']
    #     password = request.POST['password']
    #
    #     user = authenticate(request, username=username, password=password)
    #     if user:
    #         login(request, user)
    #         redirect_url = reverse_lazy('list')
    #         return HttpResponseRedirect(redirect_url)
    #
    #     return render(request, 'signin.html')
    #


def signup_view(request: HttpRequest) -> HttpResponse:
    """User sign up view"""
    if request == "POST":
        form = SignUpForm(request.POST)
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

    # if request.method == "POST":
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     confirm_password = request.POST['confirm_password']
    #
    #     if password != confirm_password:
    #         return render(request, 'signup.html')
    #     UserModel.objects.create_user(username=username, email=email, password=password)
    #
    #     redirect_url = reverse_lazy('signin')
    #
    #     return HttpResponseRedirect(redirect_url)


def profile_view(request: HttpRequest) -> HttpResponse:
    """User profile view"""
    return render(request, 'profile.html')


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    redirect_url = reverse_lazy('list')
    return HttpResponseRedirect(redirect_url)
