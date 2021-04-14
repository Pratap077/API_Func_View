from blog.models import Post
from blog.api.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
 queryset = Post.objects.all()
 serializer_class = UserSerializer
 #authentication_classes = [SessionAuthentication]
 #permission_classes = [IsAuthenticatedOrReadOnly]