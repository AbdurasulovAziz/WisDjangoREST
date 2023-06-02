from django.contrib.auth import get_user_model
from django.contrib.auth.backends import UserModel
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        style={'input_type': 'password'}
    )

    def create(self, validated_data):

        username = validated_data['email'].split('@')[0]

        user = UserModel.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=username

        )
        return user

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'password']


class UserDetailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(read_only=True)


    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'company', 'bio', 'email']



