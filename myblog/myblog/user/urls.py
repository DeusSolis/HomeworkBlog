from django.urls import path
from .views import signin_view, signup_view, profile_view


urlpatterns = [
    path('profile/<str:username>/', profile_view, name='profile'),
    path('signup/', signup_view, name='signup'),
    path('signin/', signin_view, name='signin')
]
