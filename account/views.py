from django.contrib.auth import get_user_model
from django.contrib.auth.backends import UserModel
from django.shortcuts import render
from rest_framework import generics

from account.serializers import UserSerializer, UserDetailSerializer


# Create your views here.

class UserView(generics.CreateAPIView):
    queryset = get_user_model()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = get_user_model()
    serializer_class = UserDetailSerializer

