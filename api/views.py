from django.contrib.auth import get_user_model
from rest_framework import generics, permissions


from .serializers import UserSerializer
from .permissions import IsUserSuperuserOrReadOnly
# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsUserSuperuserOrReadOnly,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
