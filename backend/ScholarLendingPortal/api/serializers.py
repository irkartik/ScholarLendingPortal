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


class BorrowRequestSerializer(serializers.ModelSerializer):
    """Serializer for BorrowRequest model"""
    user_details = UserSerializer(source='user', read_only=True)
    equipment_details = EquipmentSerializer(source='equipment', read_only=True)
    approved_by_details = UserSerializer(source='approved_by', read_only=True)

    class Meta:
        model = BorrowRequest
        fields = [
            'id', 'user', 'equipment', 'quantity', 'status',
            'request_date', 'borrow_from', 'borrow_to',
            'approved_by', 'approved_date', 'issued_date', 'returned_date',
            'purpose', 'rejection_reason', 'notes',
            'user_details', 'equipment_details', 'approved_by_details'
        ]
        read_only_fields = [
            'id', 'request_date', 'approved_by', 'approved_date',
            'issued_date', 'returned_date'
        ]

    def validate(self, data):
        borrow_from = data.get('borrow_from')
        borrow_to = data.get('borrow_to')

        # Validate dates
        if borrow_from and borrow_to:
            if borrow_to < borrow_from:
                raise serializers.ValidationError({
                    'borrow_to': 'End date must be after start date.'
                })

            if borrow_from < date.today():
                raise serializers.ValidationError({
                    'borrow_from': 'Start date cannot be in the past.'
                })

        # Validate quantity
        equipment = data.get('equipment', self.instance.equipment if self.instance else None)
        quantity = data.get('quantity', 1)

        if equipment and quantity > equipment.available_quantity:
            raise serializers.ValidationError({
                'quantity': f'Only {equipment.available_quantity} items available.'
            })

        return data


class BorrowRequestCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating borrow requests"""

    class Meta:
        model = BorrowRequest
        fields = ['equipment', 'quantity', 'borrow_from', 'borrow_to', 'purpose']

    def validate(self, data):
        borrow_from = data.get('borrow_from')
        borrow_to = data.get('borrow_to')

        if borrow_to < borrow_from:
            raise serializers.ValidationError({
                'borrow_to': 'End date must be after start date.'
            })

        if borrow_from < date.today():
            raise serializers.ValidationError({
                'borrow_from': 'Start date cannot be in the past.'
            })

        # Check equipment availability
        equipment = data.get('equipment')
        quantity = data.get('quantity', 1)

        if quantity > equipment.quantity:
            raise serializers.ValidationError({
                'quantity': f'Only {equipment.quantity} total items exist.'
            })

        # Check for overlapping approved/issued requests
        overlapping = BorrowRequest.objects.filter(
            equipment=equipment,
            status__in=['approved', 'issued'],
            borrow_from__lte=borrow_to,
            borrow_to__gte=borrow_from
        )

        total_requested = sum(req.quantity for req in overlapping)

        if total_requested + quantity > equipment.quantity:
            available = equipment.quantity - total_requested
            raise serializers.ValidationError({
                'quantity': f'Only {available} items available for the requested period.'
            })

        return data


class ApproveRejectSerializer(serializers.Serializer):
    """Serializer for approving/rejecting requests"""
    action = serializers.ChoiceField(choices=['approve', 'reject'], required=False)
    rejection_reason = serializers.CharField(required=False, allow_blank=True)
    notes = serializers.CharField(required=False, allow_blank=True)

