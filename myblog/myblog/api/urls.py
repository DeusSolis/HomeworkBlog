from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostDelete, PostUpdate

# app_name = "posts"
urlpatterns = [
    path('api/', PostList.as_view(), name='list'),
    path('api/<int:pk>/', PostDetail.as_view(), name='detail'),
    path('api/create/', PostCreate.as_view(), name='create_post'),
    path('api/delete/<int:pk>/', PostDelete.as_view(), name="delete_post"),
    path('api/update/<int:pk>/', PostUpdate.as_view(), name="update_post")
]
