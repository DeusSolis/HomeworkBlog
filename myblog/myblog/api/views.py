from rest_framework import generics
from blogApp.models import PostModel
from blogApp.serializers import PostModelSerializer


class PostList(generics.ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer


class PostCreate(generics.CreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer


class PostUpdate(generics.UpdateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer


class PostDelete(generics.DestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer
