from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Project
User = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "password")
    def validate_email(self, value):
        value = value.lower().strip()
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("An account with this email already exists.")
        return value
    def create(self, validated_data):
        email = validated_data.pop("email")
        return User.objects.create_user(username=email, email=email, **validated_data)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "first_name")
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "name", "description", "repository_url", "status", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")
