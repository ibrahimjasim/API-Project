from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Contact

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ContactSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Contact
        fields = ['owner', 'name', 'email', 'phone_number', 'created_at']