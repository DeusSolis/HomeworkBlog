from django.urls import path
from blogApp.views import post_list_view, post_detail_view


urlpatterns = [
    path('', post_list_view, name='list'),
    path('<slug:slug>/', post_detail_view, name='detail'),
]