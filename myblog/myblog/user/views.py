from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404


def signin_view(request: HttpRequest) -> HttpResponse:
    '''User sign in view'''
    return render(request, 'signin.html')

def signup_view(request: HttpRequest) -> HttpResponse:
    '''User sign up view'''
    return render(request, 'signup.html')

def profile_view(request: HttpRequest) -> HttpResponse:
    '''User profile view'''
    return render(request, 'profile.html')