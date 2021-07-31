from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model
# author = models.ForeignKey(User, on_delete=models.CASCADE)
#     update_at = models.DateTimeField(auto_now_add=True)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'create_at')
        model = Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
