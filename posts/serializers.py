from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'create_at')
        model = Post


# author = models.ForeignKey(User, on_delete=models.CASCADE)
#     update_at = models.DateTimeField(auto_now_add=True)
