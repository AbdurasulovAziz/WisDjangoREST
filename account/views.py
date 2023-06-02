from django.contrib.auth import get_user_model
from rest_framework import generics

from account.permissions import IsOwnerOrReadOnly
from account.serializers import UserSerializer, UserDetailSerializer


# Create your views here.

class UserView(generics.CreateAPIView):
    queryset = get_user_model()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = get_user_model()
    serializer_class = UserDetailSerializer
    lookup_field = 'username'
    permission_classes = [IsOwnerOrReadOnly]
