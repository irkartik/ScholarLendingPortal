from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.utils import timezone
from django.db.models import Q
from .models import User, Equipment, BorrowRequest, MaintenanceLog
from .serializers import (
    UserSerializer, LoginSerializer, EquipmentSerializer,
    BorrowRequestSerializer, BorrowRequestCreateSerializer,
    ApproveRejectSerializer, MaintenanceLogSerializer
)
from .permissions import IsAdmin, IsStaffOrAdmin


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """Register a new user"""
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


class BorrowRequestViewSet(viewsets.ModelViewSet):
    """ViewSet for BorrowRequest operations"""
    queryset = BorrowRequest.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return BorrowRequestCreateSerializer
        return BorrowRequestSerializer

    def get_queryset(self):
        """Filter requests based on user role and query parameters"""
        user = self.request.user
        queryset = BorrowRequest.objects.all()

        # Students can only see their own requests
        if user.role == 'student':
            queryset = queryset.filter(user=user)

        # Filter by status
        request_status = self.request.query_params.get('status', None)
        if request_status:
            queryset = queryset.filter(status=request_status)

        # Filter by user (for admins/staff)
        user_id = self.request.query_params.get('user', None)
        if user_id and user.role in ['staff', 'admin']:
            queryset = queryset.filter(user_id=user_id)

        # Filter by equipment
        equipment_id = self.request.query_params.get('equipment', None)
        if equipment_id:
            queryset = queryset.filter(equipment_id=equipment_id)

        return queryset.select_related('user', 'equipment', 'approved_by')

    def perform_create(self, serializer):
        """Create a new borrow request"""
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsStaffOrAdmin])
    def approve(self, request, pk=None):
        """Approve a borrow request"""
        borrow_request = self.get_object()

        if borrow_request.status != 'pending':
            return Response(
                {'error': 'Only pending requests can be approved.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ApproveRejectSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Check equipment availability for the requested period
        overlapping = BorrowRequest.objects.filter(
            equipment=borrow_request.equipment,
            status__in=['approved', 'issued'],
            borrow_from__lte=borrow_request.borrow_to,
            borrow_to__gte=borrow_request.borrow_from
        ).exclude(pk=borrow_request.pk)

        total_requested = sum(req.quantity for req in overlapping)

        if total_requested + borrow_request.quantity > borrow_request.equipment.quantity:
            available = borrow_request.equipment.quantity - total_requested
            return Response(
                {'error': f'Only {available} items available for the requested period.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        borrow_request.status = 'approved'
        borrow_request.approved_by = request.user
        borrow_request.approved_date = timezone.now()
        borrow_request.notes = serializer.validated_data.get('notes', '')
        borrow_request.save()

        return Response(
            BorrowRequestSerializer(borrow_request).data,
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsStaffOrAdmin])
    def reject(self, request, pk=None):
        """Reject a borrow request"""
        borrow_request = self.get_object()

        if borrow_request.status != 'pending':
            return Response(
                {'error': 'Only pending requests can be rejected.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ApproveRejectSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        borrow_request.status = 'rejected'
        borrow_request.approved_by = request.user
        borrow_request.approved_date = timezone.now()
        borrow_request.rejection_reason = serializer.validated_data.get('rejection_reason', '')
        borrow_request.notes = serializer.validated_data.get('notes', '')
        borrow_request.save()

        return Response(
            BorrowRequestSerializer(borrow_request).data,
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsStaffOrAdmin])
    def issue(self, request, pk=None):
        """Mark request as issued (equipment given to user)"""
        borrow_request = self.get_object()

        if borrow_request.status != 'approved':
            return Response(
                {'error': 'Only approved requests can be issued.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Update equipment availability
        equipment = borrow_request.equipment
        if equipment.available_quantity < borrow_request.quantity:
            return Response(
                {'error': 'Not enough equipment available.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        equipment.available_quantity -= borrow_request.quantity
        equipment.save()

        borrow_request.status = 'issued'
        borrow_request.issued_date = timezone.now()
        borrow_request.save()

        return Response(
            BorrowRequestSerializer(borrow_request).data,
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsStaffOrAdmin])
    def mark_returned(self, request, pk=None):
        """Mark request as returned"""
        borrow_request = self.get_object()

        if borrow_request.status != 'issued':
            return Response(
                {'error': 'Only issued requests can be marked as returned.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Update equipment availability
        equipment = borrow_request.equipment
        equipment.available_quantity += borrow_request.quantity
        equipment.save()

        borrow_request.status = 'returned'
        borrow_request.returned_date = timezone.now()
        borrow_request.save()

        return Response(
            BorrowRequestSerializer(borrow_request).data,
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['get'])
    def my_requests(self, request):
        """Get current user's borrow requests"""
        requests = BorrowRequest.objects.filter(user=request.user)
        serializer = BorrowRequestSerializer(requests, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def pending_approvals(self, request):
        """Get pending requests for approval (staff/admin only)"""
        if request.user.role not in ['staff', 'admin']:
            return Response(
                {'error': 'Permission denied.'},
                status=status.HTTP_403_FORBIDDEN
            )

        requests = BorrowRequest.objects.filter(status='pending')
        serializer = BorrowRequestSerializer(requests, many=True)
        return Response(serializer.data)

class MaintenanceLogViewSet(viewsets.ModelViewSet):
    """ViewSet for MaintenanceLog operations"""
    queryset = MaintenanceLog.objects.all()
    serializer_class = MaintenanceLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter logs based on query parameters"""
        queryset = MaintenanceLog.objects.all()

        # Filter by equipment
        equipment_id = self.request.query_params.get('equipment', None)
        if equipment_id:
            queryset = queryset.filter(equipment_id=equipment_id)

        # Filter by log type
        log_type = self.request.query_params.get('log_type', None)
        if log_type:
            queryset = queryset.filter(log_type=log_type)

        return queryset.select_related('equipment', 'reported_by')

    def perform_create(self, serializer):
        """Create a new maintenance log"""
        serializer.save(reported_by=self.request.user)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_stats(request):
    """Get dashboard statistics"""
    total_equipment = Equipment.objects.count()
    available_equipment = Equipment.objects.filter(available_quantity__gt=0).count()

    pending_requests = BorrowRequest.objects.filter(status='pending').count()
    approved_requests = BorrowRequest.objects.filter(status='approved').count()
    issued_requests = BorrowRequest.objects.filter(status='issued').count()

    if request.user.role == 'student':
        my_requests = BorrowRequest.objects.filter(user=request.user).count()
        my_pending = BorrowRequest.objects.filter(user=request.user, status='pending').count()
        my_issued = BorrowRequest.objects.filter(user=request.user, status='issued').count()

        return Response({
            'total_equipment': total_equipment,
            'available_equipment': available_equipment,
            'my_requests': my_requests,
            'my_pending': my_pending,
            'my_issued': my_issued,
        })

    return Response({
        'total_equipment': total_equipment,
        'available_equipment': available_equipment,
        'pending_requests': pending_requests,
        'approved_requests': approved_requests,
        'issued_requests': issued_requests,
    })

