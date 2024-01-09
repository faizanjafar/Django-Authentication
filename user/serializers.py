from rest_framework import serializers
from .models import UserAccount
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = "__all__"

    def create(self, validated_data):
        user = UserAccount.objects.create_user(**validated_data)
        return user
