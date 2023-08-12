# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from django.contrib.auth.password_validation import validate_password

# from rest_framework import serializers

# from .models import *

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("__all__")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        password = validated_data.get("password")
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance

    def validate(self, attrs):
        nickname = attrs.get("nickname", None)
        if User.objects.filter(nickname=nickname).exists():
            raise serializers.ValidationError("nickname already exists")

        password = attrs.get("password", None)
        validate_password(password)

        return attrs

class LoginUserSerializer(serializers.Serializer):
    nickname = serializers.CharField()
    password = serializers.CharField()