from rest_framework import generics
from blogApp.models import PostModel
from blogApp.serializers import PostModelSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import UserPermission


class PostList(generics.ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer


class PostCreate(generics.CreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer
    permission_classes = [IsAuthenticated, UserPermission]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostUpdate(generics.UpdateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer
    permission_classes = [IsAuthenticated, UserPermission]


class PostDelete(generics.DestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer
    permission_classes = [IsAuthenticated, UserPermission]
