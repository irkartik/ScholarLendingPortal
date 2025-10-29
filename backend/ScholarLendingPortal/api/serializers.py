from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Equipment, BorrowRequest
from datetime import date


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'role', 'phone_number']
        read_only_fields = ['id']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role=validated_data.get('role', 'student'),
            phone_number=validated_data.get('phone_number', '')
        )
        return user

class LoginSerializer(serializers.Serializer):
    """Serializer for user login"""
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError('User account is disabled.')
                data['user'] = user
            else:
                raise serializers.ValidationError('Unable to login with provided credentials.')
        else:
            raise serializers.ValidationError('Must include "username" and "password".')

        return data

class EquipmentSerializer(serializers.ModelSerializer):
    """Serializer for Equipment model"""
    is_available = serializers.BooleanField(read_only=True)

    class Meta:
        model = Equipment
        fields = [
            'id', 'name', 'category', 'description', 'condition',
            'quantity', 'available_quantity', 'is_available',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        # Ensure available_quantity doesn't exceed quantity
        quantity = data.get('quantity', self.instance.quantity if self.instance else 0)
        available_quantity = data.get('available_quantity', self.instance.available_quantity if self.instance else 0)

        if available_quantity > quantity:
            raise serializers.ValidationError({
                'available_quantity': 'Available quantity cannot exceed total quantity.'
            })

        return data