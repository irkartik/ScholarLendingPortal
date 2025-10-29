from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'equipment', views.EquipmentViewSet, basename='equipment')

urlpatterns = [
    path('auth/register/', views.register, name='register'),
    path('auth/login/', views.login, name='login'),
    path('auth/user/', views.current_user, name='current_user'),
    path('', include(router.urls)),
]