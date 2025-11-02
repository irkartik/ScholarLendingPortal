from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'equipment', views.EquipmentViewSet, basename='equipment')
router.register(r'borrow-requests', views.BorrowRequestViewSet, basename='borrow-request')
router.register(r'maintenance-logs', views.MaintenanceLogViewSet, basename='maintenance-log')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', views.register, name='register'),
    path('auth/login/', views.login, name='login'),
    path('auth/user/', views.current_user, name='current-user'),
    path('dashboard/stats/', views.dashboard_stats, name='dashboard-stats'),
]

