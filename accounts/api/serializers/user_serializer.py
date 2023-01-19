from django.contrib.auth.models import Group, Permission
from models.user_model import User
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'is_active', 'is_staff', 'date_joined']
    



