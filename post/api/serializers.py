from rest_framework.serializers import ModelSerializer
from post.models import Post

class PostSerializerGet(ModelSerializer):
    class Meta: 
        model = Post
        fields = ['title', 'description', 'order', 'created_at']


class PostSerializerPost(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description', 'order']