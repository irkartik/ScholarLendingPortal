from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import User, Equipment, BorrowRequest
from .permissions import IsAdmin

from .serializers import (
    UserSerializer,
    LoginSerializer,
    EquipmentSerializer
)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """API endpoint for user registration"""
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """Login user and return tokens"""
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    """Get current logged in user details"""
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class EquipmentViewSet(viewsets.ModelViewSet):
    """ViewSet for Equipment CRUD operations"""
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def get_permissions(self):
        """Set permissions based on action"""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        """Filter equipment based on query parameters"""
        queryset = Equipment.objects.all()

        # Search by name
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(name__icontains=search)

        # Filter by category
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category=category)

        # Filter by availability
        available = self.request.query_params.get('available', None)
        if available is not None:
            if available.lower() == 'true':
                queryset = queryset.filter(available_quantity__gt=0)
            elif available.lower() == 'false':
                queryset = queryset.filter(available_quantity=0)

        # Filter by condition
        condition = self.request.query_params.get('condition', None)
        if condition:
            queryset = queryset.filter(condition=condition)

        return queryset

    @action(detail=False, methods=['get'])
    def categories(self, request):
        """Get list of equipment categories"""
        categories = [
            {'value': choice[0], 'label': choice[1]}
            for choice in Equipment.CATEGORY_CHOICES
        ]
        return Response(categories)

    @action(detail=False, methods=['get'])
    def conditions(self, request):
        """Get list of equipment conditions"""
        conditions = [
            {'value': choice[0], 'label': choice[1]}
            for choice in Equipment.CONDITION_CHOICES
        ]
        return Response(conditions)
