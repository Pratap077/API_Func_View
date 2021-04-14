from blog.models import Post
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
 class Meta:
  model = Post
  fields = ['id', 'title','desc']