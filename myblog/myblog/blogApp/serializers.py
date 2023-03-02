from rest_framework import serializers

from .models import PostModel, CategoryModel


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('id', 'title')


class PostModelSerializer(serializers.ModelSerializer):
    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = PostModel
        fields = ('id', 'name', 'category', 'content', 'created_at', 'updated_at', 'owner')


