from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Equipment, LendingRecord
from .serializers import EquipmentSerializer, LendingRecordSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Equipment instances.
    """
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    @action(detail=True, methods=['get'])
    def available(self, request, pk=None):
        """Get available quantity for specific equipment"""
        equipment = self.get_object()
        return Response({
            'id': equipment.id,
            'name': equipment.name,
            'quantity_available': equipment.quantity_available
        })


class LendingRecordViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing LendingRecord instances.
    """
    queryset = LendingRecord.objects.all()
    serializer_class = LendingRecordSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned records by filtering against
        query parameters in the URL.
        """
        queryset = LendingRecord.objects.all()
        user_id = self.request.query_params.get('user', None)
        status = self.request.query_params.get('status', None)
        
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        if status is not None:
            queryset = queryset.filter(status=status)
        
        return queryset

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        """Approve a lending request"""
        record = self.get_object()
        record.status = 'approved'
        record.save()
        serializer = self.get_serializer(record)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def return_equipment(self, request, pk=None):
        """Mark equipment as returned"""
        record = self.get_object()
        record.status = 'returned'
        from django.utils import timezone
        record.return_date = timezone.now()
        record.save()
        serializer = self.get_serializer(record)
        return Response(serializer.data)

