from django.contrib.auth import get_user_model
from django.contrib.auth.backends import UserModel
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        style={'input_type': 'password'}
    )

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['email']

        )
        return user

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'password']


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        exclude = ['password']



