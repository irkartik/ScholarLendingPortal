from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils import timezone
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from datetime import date, timedelta
from decimal import Decimal

from .models import User, Equipment, BorrowRequest, MaintenanceLog
from .serializers import (
    UserSerializer, LoginSerializer, EquipmentSerializer,
    BorrowRequestSerializer, BorrowRequestCreateSerializer,
    MaintenanceLogSerializer
)

User = get_user_model()


# ==================== MODEL TESTS ====================

class UserModelTest(TestCase):
    """Test cases for User model"""

    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
            'role': 'student',
            'phone_number': '1234567890'
        }

    def test_create_user(self):
        """Test creating a user"""
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.role, 'student')
        self.assertTrue(user.check_password('testpass123'))

    def test_user_default_role(self):
        """Test user default role is student"""
        user = User.objects.create_user(
            username='student1',
            email='student@test.com',
            password='pass123'
        )
        self.assertEqual(user.role, 'student')

    def test_user_str_method(self):
        """Test user string representation"""
        user = User.objects.create_user(**self.user_data)
        expected_str = f"{user.username} ({user.get_role_display()})"
        self.assertEqual(str(user), expected_str)

    def test_create_admin_user(self):
        """Test creating an admin user"""
        admin_data = self.user_data.copy()
        admin_data['role'] = 'admin'
        admin = User.objects.create_user(**admin_data)
        self.assertEqual(admin.role, 'admin')

    def test_create_staff_user(self):
        """Test creating a staff user"""
        staff_data = self.user_data.copy()
        staff_data['role'] = 'staff'
        staff = User.objects.create_user(**staff_data)
        self.assertEqual(staff.role, 'staff')


class EquipmentModelTest(TestCase):
    """Test cases for Equipment model"""

    def setUp(self):
        self.equipment_data = {
            'name': 'Basketball',
            'category': 'sports',
            'description': 'Standard basketball',
            'condition': 'good',
            'quantity': 10,
            'available_quantity': 10
        }

    def test_create_equipment(self):
        """Test creating equipment"""
        equipment = Equipment.objects.create(**self.equipment_data)
        self.assertEqual(equipment.name, 'Basketball')
        self.assertEqual(equipment.quantity, 10)
        self.assertEqual(equipment.available_quantity, 10)

    def test_equipment_str_method(self):
        """Test equipment string representation"""
        equipment = Equipment.objects.create(**self.equipment_data)
        expected_str = f"Basketball (10/10 available)"
        self.assertEqual(str(equipment), expected_str)

    def test_equipment_is_available_property(self):
        """Test is_available property"""
        equipment = Equipment.objects.create(**self.equipment_data)
        self.assertTrue(equipment.is_available)

        equipment.available_quantity = 0
        equipment.save()
        self.assertFalse(equipment.is_available)

    def test_available_quantity_exceeds_quantity_on_save(self):
        """Test that available_quantity is adjusted if it exceeds quantity"""
        equipment = Equipment.objects.create(
            name='Camera',
            category='camera',
            quantity=5,
            available_quantity=10  # Intentionally higher
        )
        # Should be adjusted to quantity
        self.assertEqual(equipment.available_quantity, 5)

    def test_equipment_default_values(self):
        """Test equipment default values"""
        equipment = Equipment.objects.create(
            name='Microscope',
            category='lab'
        )
        self.assertEqual(equipment.condition, 'good')
        self.assertEqual(equipment.quantity, 1)
        self.assertEqual(equipment.available_quantity, 1)

    def test_equipment_ordering(self):
        """Test equipment is ordered by created_at descending"""
        eq1 = Equipment.objects.create(name='Item1', category='sports')
        eq2 = Equipment.objects.create(name='Item2', category='sports')

        equipment_list = list(Equipment.objects.all())
        self.assertEqual(equipment_list[0], eq2)
        self.assertEqual(equipment_list[1], eq1)


class BorrowRequestModelTest(TestCase):
    """Test cases for BorrowRequest model"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='student1',
            email='student@test.com',
            password='pass123'
        )
        self.staff = User.objects.create_user(
            username='staff1',
            email='staff@test.com',
            password='pass123',
            role='staff'
        )
        self.equipment = Equipment.objects.create(
            name='Basketball',
            category='sports',
            quantity=5,
            available_quantity=5
        )

    def test_create_borrow_request(self):
        """Test creating a borrow request"""
        borrow_request = BorrowRequest.objects.create(
            user=self.user,
            equipment=self.equipment,
            quantity=2,
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=3),
            purpose='For practice'
        )
        self.assertEqual(borrow_request.status, 'pending')
        self.assertEqual(borrow_request.quantity, 2)

    def test_borrow_request_str_method(self):
        """Test borrow request string representation"""
        borrow_request = BorrowRequest.objects.create(
            user=self.user,
            equipment=self.equipment,
            quantity=1,
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=3)
        )
        expected_str = f"{self.user.username} - {self.equipment.name} (pending)"
        self.assertEqual(str(borrow_request), expected_str)

    def test_borrow_request_validation_end_before_start(self):
        """Test validation: end date must be after start date"""
        with self.assertRaises(ValidationError):
            borrow_request = BorrowRequest(
                user=self.user,
                equipment=self.equipment,
                quantity=1,
                borrow_from=date.today() + timedelta(days=5),
                borrow_to=date.today() + timedelta(days=2)
            )
            borrow_request.save()

    def test_overlapping_bookings_validation(self):
        """Test validation for overlapping bookings"""
        # Create first approved request
        BorrowRequest.objects.create(
            user=self.user,
            equipment=self.equipment,
            quantity=3,
            status='approved',
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=5)
        )

        # Try to create overlapping request that exceeds quantity
        with self.assertRaises(ValidationError):
            borrow_request = BorrowRequest(
                user=self.user,
                equipment=self.equipment,
                quantity=3,  # 3 + 3 = 6 > 5 total
                status='approved',
                borrow_from=date.today() + timedelta(days=3),
                borrow_to=date.today() + timedelta(days=7)
            )
            borrow_request.save()

    def test_pending_requests_do_not_block_availability(self):
        """Test that pending requests don't block availability"""
        # Create pending request
        BorrowRequest.objects.create(
            user=self.user,
            equipment=self.equipment,
            quantity=5,
            status='pending',
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=5)
        )

        # Should be able to approve another request for same period since first is pending
        borrow_request = BorrowRequest.objects.create(
            user=self.user,
            equipment=self.equipment,
            quantity=5,
            status='pending',
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=5)
        )
        self.assertEqual(borrow_request.status, 'pending')


class MaintenanceLogModelTest(TestCase):
    """Test cases for MaintenanceLog model"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='staff1',
            email='staff@test.com',
            password='pass123',
            role='staff'
        )
        self.equipment = Equipment.objects.create(
            name='Camera',
            category='camera',
            quantity=3
        )

    def test_create_maintenance_log(self):
        """Test creating a maintenance log"""
        log = MaintenanceLog.objects.create(
            equipment=self.equipment,
            log_type='damage',
            description='Lens scratched',
            reported_by=self.user,
            cost=Decimal('50.00')
        )
        self.assertEqual(log.log_type, 'damage')
        self.assertEqual(log.cost, Decimal('50.00'))

    def test_maintenance_log_str_method(self):
        """Test maintenance log string representation"""
        log = MaintenanceLog.objects.create(
            equipment=self.equipment,
            log_type='repair',
            description='Fixed lens',
            reported_by=self.user
        )
        self.assertIn(self.equipment.name, str(log))
        self.assertIn('Repair', str(log))


# ==================== SERIALIZER TESTS ====================

class UserSerializerTest(TestCase):
    """Test cases for UserSerializer"""

    def test_user_serializer_create(self):
        """Test creating user through serializer"""
        data = {
            'username': 'newuser',
            'email': 'new@test.com',
            'password': 'newpass123',
            'first_name': 'New',
            'last_name': 'User',
            'role': 'student',
            'phone_number': '1234567890'
        }
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, 'newuser')
        self.assertTrue(user.check_password('newpass123'))

    def test_user_serializer_password_write_only(self):
        """Test that password is write-only"""
        user = User.objects.create_user(
            username='test',
            password='pass123'
        )
        serializer = UserSerializer(user)
        self.assertNotIn('password', serializer.data)


class LoginSerializerTest(TestCase):
    """Test cases for LoginSerializer"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_login_serializer_valid_credentials(self):
        """Test login with valid credentials"""
        data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        serializer = LoginSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['user'], self.user)

    def test_login_serializer_invalid_credentials(self):
        """Test login with invalid credentials"""
        data = {
            'username': 'testuser',
            'password': 'wrongpass'
        }
        serializer = LoginSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_login_serializer_inactive_user(self):
        """Test login with inactive user"""
        self.user.is_active = False
        self.user.save()

        data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        serializer = LoginSerializer(data=data)
        self.assertFalse(serializer.is_valid())


class EquipmentSerializerTest(TestCase):
    """Test cases for EquipmentSerializer"""

    def test_equipment_serializer_create(self):
        """Test creating equipment through serializer"""
        data = {
            'name': 'Football',
            'category': 'sports',
            'description': 'Standard football',
            'condition': 'good',
            'quantity': 10,
            'available_quantity': 10
        }
        serializer = EquipmentSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        equipment = serializer.save()
        self.assertEqual(equipment.name, 'Football')

    def test_equipment_serializer_validation_available_exceeds_total(self):
        """Test validation: available_quantity cannot exceed quantity"""
        data = {
            'name': 'Football',
            'category': 'sports',
            'quantity': 5,
            'available_quantity': 10
        }
        serializer = EquipmentSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('available_quantity', serializer.errors)


class BorrowRequestSerializerTest(TestCase):
    """Test cases for BorrowRequestSerializer"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='student1',
            password='pass123'
        )
        self.equipment = Equipment.objects.create(
            name='Camera',
            category='camera',
            quantity=3,
            available_quantity=3
        )

    def test_borrow_request_create_serializer_valid(self):
        """Test creating borrow request with valid data"""
        data = {
            'equipment': self.equipment.id,
            'quantity': 2,
            'borrow_from': date.today() + timedelta(days=1),
            'borrow_to': date.today() + timedelta(days=3),
            'purpose': 'School project'
        }
        serializer = BorrowRequestCreateSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_borrow_request_serializer_past_date_validation(self):
        """Test validation: cannot borrow from past date"""
        data = {
            'equipment': self.equipment.id,
            'quantity': 1,
            'borrow_from': date.today() - timedelta(days=1),
            'borrow_to': date.today() + timedelta(days=3),
            'purpose': 'Test'
        }
        serializer = BorrowRequestCreateSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('borrow_from', serializer.errors)

    def test_borrow_request_serializer_end_before_start_validation(self):
        """Test validation: end date must be after start date"""
        data = {
            'equipment': self.equipment.id,
            'quantity': 1,
            'borrow_from': date.today() + timedelta(days=5),
            'borrow_to': date.today() + timedelta(days=2),
            'purpose': 'Test'
        }
        serializer = BorrowRequestCreateSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('borrow_to', serializer.errors)

    def test_borrow_request_serializer_quantity_exceeds_total(self):
        """Test validation: cannot request more than total quantity"""
        data = {
            'equipment': self.equipment.id,
            'quantity': 10,  # Equipment only has 3
            'borrow_from': date.today() + timedelta(days=1),
            'borrow_to': date.today() + timedelta(days=3),
            'purpose': 'Test'
        }
        serializer = BorrowRequestCreateSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('quantity', serializer.errors)


# ==================== VIEW TESTS ====================

class AuthenticationViewTest(APITestCase):
    """Test cases for authentication views"""

    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        """Test user registration"""
        url = '/api/auth/register/'
        data = {
            'username': 'newuser',
            'email': 'new@test.com',
            'password': 'newpass123',
            'first_name': 'New',
            'last_name': 'User',
            'role': 'student'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertEqual(response.data['user']['username'], 'newuser')

    def test_register_user_duplicate_username(self):
        """Test registration with duplicate username"""
        User.objects.create_user(username='existing', password='pass123')

        url = '/api/auth/register/'
        data = {
            'username': 'existing',
            'password': 'newpass123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_user(self):
        """Test user login"""
        user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        url = '/api/auth/login/'
        data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_invalid_credentials(self):
        """Test login with invalid credentials"""
        User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        url = '/api/auth/login/'
        data = {
            'username': 'testuser',
            'password': 'wrongpass'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_current_user_authenticated(self):
        """Test getting current user details when authenticated"""
        user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.force_authenticate(user=user)

        url = '/api/auth/user/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')

    def test_current_user_unauthenticated(self):
        """Test getting current user without authentication"""
        url = '/api/auth/user/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class EquipmentViewSetTest(APITestCase):
    """Test cases for EquipmentViewSet"""

    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_user(
            username='admin',
            password='pass123',
            role='admin'
        )
        self.student = User.objects.create_user(
            username='student',
            password='pass123',
            role='student'
        )
        self.equipment = Equipment.objects.create(
            name='Basketball',
            category='sports',
            quantity=10,
            available_quantity=8
        )

    def test_list_equipment_authenticated(self):
        """Test listing equipment as authenticated user"""
        self.client.force_authenticate(user=self.student)
        url = '/api/equipment/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_equipment_unauthenticated(self):
        """Test listing equipment without authentication"""
        url = '/api/equipment/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_equipment(self):
        """Test retrieving single equipment"""
        self.client.force_authenticate(user=self.student)
        url = f'/api/equipment/{self.equipment.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Basketball')

    def test_create_equipment_as_admin(self):
        """Test creating equipment as admin"""
        self.client.force_authenticate(user=self.admin)
        url = '/api/equipment/'
        data = {
            'name': 'Football',
            'category': 'sports',
            'quantity': 5,
            'available_quantity': 5
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Equipment.objects.count(), 2)

    def test_create_equipment_as_student(self):
        """Test creating equipment as student (should fail)"""
        self.client.force_authenticate(user=self.student)
        url = '/api/equipment/'
        data = {
            'name': 'Football',
            'category': 'sports',
            'quantity': 5
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_equipment_as_admin(self):
        """Test updating equipment as admin"""
        self.client.force_authenticate(user=self.admin)
        url = f'/api/equipment/{self.equipment.id}/'
        data = {
            'name': 'Updated Basketball',
            'category': 'sports',
            'quantity': 15,
            'available_quantity': 10
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.equipment.refresh_from_db()
        self.assertEqual(self.equipment.quantity, 15)

    def test_delete_equipment_as_admin(self):
        """Test deleting equipment as admin"""
        self.client.force_authenticate(user=self.admin)
        url = f'/api/equipment/{self.equipment.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Equipment.objects.count(), 0)

    def test_filter_equipment_by_category(self):
        """Test filtering equipment by category"""
        Equipment.objects.create(
            name='Microscope',
            category='lab',
            quantity=5
        )
        self.client.force_authenticate(user=self.student)
        url = '/api/equipment/?category=sports'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['category'], 'sports')

    def test_filter_equipment_by_availability(self):
        """Test filtering equipment by availability"""
        Equipment.objects.create(
            name='Out of Stock Item',
            category='sports',
            quantity=5,
            available_quantity=0
        )
        self.client.force_authenticate(user=self.student)
        url = '/api/equipment/?available=true'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Only equipment with available_quantity > 0
        for item in response.data:
            self.assertGreater(item['available_quantity'], 0)

    def test_search_equipment_by_name(self):
        """Test searching equipment by name"""
        Equipment.objects.create(
            name='Football',
            category='sports',
            quantity=5
        )
        self.client.force_authenticate(user=self.student)
        url = '/api/equipment/?search=basket'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertIn('basket', response.data[0]['name'].lower())

    def test_get_equipment_categories(self):
        """Test getting list of equipment categories"""
        self.client.force_authenticate(user=self.student)
        url = '/api/equipment/categories/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreater(len(response.data), 0)

    def test_get_equipment_conditions(self):
        """Test getting list of equipment conditions"""
        self.client.force_authenticate(user=self.student)
        url = '/api/equipment/conditions/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreater(len(response.data), 0)


class BorrowRequestViewSetTest(APITestCase):
    """Test cases for BorrowRequestViewSet"""

    def setUp(self):
        self.client = APIClient()
        self.student = User.objects.create_user(
            username='student',
            password='pass123',
            role='student'
        )
        self.staff = User.objects.create_user(
            username='staff',
            password='pass123',
            role='staff'
        )
        self.admin = User.objects.create_user(
            username='admin',
            password='pass123',
            role='admin'
        )
        self.equipment = Equipment.objects.create(
            name='Camera',
            category='camera',
            quantity=5,
            available_quantity=5
        )

    def test_create_borrow_request_as_student(self):
        """Test creating a borrow request as student"""
        self.client.force_authenticate(user=self.student)
        url = '/api/borrow-requests/'
        data = {
            'equipment': self.equipment.id,
            'quantity': 2,
            'borrow_from': str(date.today() + timedelta(days=1)),
            'borrow_to': str(date.today() + timedelta(days=3)),
            'purpose': 'School project'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Verify the request was created in database
        borrow_request = BorrowRequest.objects.get(user=self.student)
        self.assertEqual(borrow_request.status, 'pending')
        self.assertEqual(borrow_request.quantity, 2)

    def test_list_borrow_requests_as_student(self):
        """Test student can only see their own requests"""
        other_student = User.objects.create_user(
            username='other',
            password='pass123'
        )
        # Create requests for both students
        BorrowRequest.objects.create(
            user=self.student,
            equipment=self.equipment,
            quantity=1,
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=3)
        )
        BorrowRequest.objects.create(
            user=other_student,
            equipment=self.equipment,
            quantity=1,
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=3)
        )

        self.client.force_authenticate(user=self.student)
        url = '/api/borrow-requests/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_borrow_requests_as_staff(self):
        """Test staff can see all requests"""
        BorrowRequest.objects.create(
            user=self.student,
            equipment=self.equipment,
            quantity=1,
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=3)
        )

        self.client.force_authenticate(user=self.staff)
        url = '/api/borrow-requests/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_approve_borrow_request_as_staff(self):
        """Test approving a borrow request as staff"""
        borrow_request = BorrowRequest.objects.create(
            user=self.student,
            equipment=self.equipment,
            quantity=2,
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=3)
        )

        self.client.force_authenticate(user=self.staff)
        url = f'/api/borrow-requests/{borrow_request.id}/approve/'
        data = {'notes': 'Approved'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        borrow_request.refresh_from_db()
        self.assertEqual(borrow_request.status, 'approved')
        self.assertEqual(borrow_request.approved_by, self.staff)

    def test_approve_borrow_request_as_student(self):
        """Test student cannot approve requests"""
        borrow_request = BorrowRequest.objects.create(
            user=self.student,
            equipment=self.equipment,
            quantity=2,
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=3)
        )

        self.client.force_authenticate(user=self.student)
        url = f'/api/borrow-requests/{borrow_request.id}/approve/'
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_reject_borrow_request_as_staff(self):
        """Test rejecting a borrow request as staff"""
        borrow_request = BorrowRequest.objects.create(
            user=self.student,
            equipment=self.equipment,
            quantity=2,
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=3)
        )

        self.client.force_authenticate(user=self.staff)
        url = f'/api/borrow-requests/{borrow_request.id}/reject/'
        data = {'rejection_reason': 'Not available'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        borrow_request.refresh_from_db()
        self.assertEqual(borrow_request.status, 'rejected')

    def test_approve_non_pending_request_fails(self):
        """Test cannot approve non-pending request"""
        borrow_request = BorrowRequest.objects.create(
            user=self.student,
            equipment=self.equipment,
            quantity=2,
            status='approved',
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=3)
        )

        self.client.force_authenticate(user=self.staff)
        url = f'/api/borrow-requests/{borrow_request.id}/approve/'
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_issue_equipment_as_staff(self):
        """Test issuing equipment as staff"""
        borrow_request = BorrowRequest.objects.create(
            user=self.student,
            equipment=self.equipment,
            quantity=2,
            status='approved',
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=3)
        )

        self.client.force_authenticate(user=self.staff)
        url = f'/api/borrow-requests/{borrow_request.id}/issue/'
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        borrow_request.refresh_from_db()
        self.assertEqual(borrow_request.status, 'issued')

        self.equipment.refresh_from_db()
        self.assertEqual(self.equipment.available_quantity, 3)  # 5 - 2

    def test_issue_non_approved_request_fails(self):
        """Test cannot issue non-approved request"""
        borrow_request = BorrowRequest.objects.create(
            user=self.student,
            equipment=self.equipment,
            quantity=2,
            status='pending',
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=3)
        )

        self.client.force_authenticate(user=self.staff)
        url = f'/api/borrow-requests/{borrow_request.id}/issue/'
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_mark_returned_as_staff(self):
        """Test marking equipment as returned"""
        borrow_request = BorrowRequest.objects.create(
            user=self.student,
            equipment=self.equipment,
            quantity=2,
            status='issued',
            borrow_from=date.today(),
            borrow_to=date.today() + timedelta(days=3)
        )
        # Simulate issuing
        self.equipment.available_quantity = 3
        self.equipment.save()

        self.client.force_authenticate(user=self.staff)
        url = f'/api/borrow-requests/{borrow_request.id}/mark_returned/'
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        borrow_request.refresh_from_db()
        self.assertEqual(borrow_request.status, 'returned')

        self.equipment.refresh_from_db()
        self.assertEqual(self.equipment.available_quantity, 5)  # 3 + 2

    def test_get_my_requests(self):
        """Test getting current user's requests"""
        BorrowRequest.objects.create(
            user=self.student,
            equipment=self.equipment,
            quantity=1,
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=3)
        )

        self.client.force_authenticate(user=self.student)
        url = '/api/borrow-requests/my_requests/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_pending_approvals_as_staff(self):
        """Test getting pending approvals as staff"""
        BorrowRequest.objects.create(
            user=self.student,
            equipment=self.equipment,
            quantity=1,
            status='pending',
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=3)
        )

        self.client.force_authenticate(user=self.staff)
        url = '/api/borrow-requests/pending_approvals/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_pending_approvals_as_student_fails(self):
        """Test student cannot get pending approvals"""
        self.client.force_authenticate(user=self.student)
        url = '/api/borrow-requests/pending_approvals/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_filter_borrow_requests_by_status(self):
        """Test filtering borrow requests by status"""
        BorrowRequest.objects.create(
            user=self.student,
            equipment=self.equipment,
            quantity=1,
            status='pending',
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=3)
        )
        BorrowRequest.objects.create(
            user=self.student,
            equipment=self.equipment,
            quantity=1,
            status='approved',
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=3)
        )

        self.client.force_authenticate(user=self.staff)
        url = '/api/borrow-requests/?status=pending'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for request in response.data:
            self.assertEqual(request['status'], 'pending')


class MaintenanceLogViewSetTest(APITestCase):
    """Test cases for MaintenanceLogViewSet"""

    def setUp(self):
        self.client = APIClient()
        self.staff = User.objects.create_user(
            username='staff',
            password='pass123',
            role='staff'
        )
        self.student = User.objects.create_user(
            username='student',
            password='pass123',
            role='student'
        )
        self.equipment = Equipment.objects.create(
            name='Camera',
            category='camera',
            quantity=3
        )

    def test_create_maintenance_log(self):
        """Test creating a maintenance log"""
        self.client.force_authenticate(user=self.staff)
        url = '/api/maintenance-logs/'
        data = {
            'equipment': self.equipment.id,
            'log_type': 'damage',
            'description': 'Lens scratched',
            'cost': '50.00'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MaintenanceLog.objects.count(), 1)

    def test_list_maintenance_logs(self):
        """Test listing maintenance logs"""
        MaintenanceLog.objects.create(
            equipment=self.equipment,
            log_type='repair',
            description='Fixed lens',
            reported_by=self.staff
        )

        self.client.force_authenticate(user=self.staff)
        url = '/api/maintenance-logs/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_maintenance_logs_by_equipment(self):
        """Test filtering logs by equipment"""
        other_equipment = Equipment.objects.create(
            name='Microscope',
            category='lab',
            quantity=2
        )
        MaintenanceLog.objects.create(
            equipment=self.equipment,
            log_type='damage',
            description='Camera damage',
            reported_by=self.staff
        )
        MaintenanceLog.objects.create(
            equipment=other_equipment,
            log_type='repair',
            description='Microscope repair',
            reported_by=self.staff
        )

        self.client.force_authenticate(user=self.staff)
        url = f'/api/maintenance-logs/?equipment={self.equipment.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_maintenance_logs_by_type(self):
        """Test filtering logs by type"""
        MaintenanceLog.objects.create(
            equipment=self.equipment,
            log_type='damage',
            description='Damage report',
            reported_by=self.staff
        )
        MaintenanceLog.objects.create(
            equipment=self.equipment,
            log_type='repair',
            description='Repair report',
            reported_by=self.staff
        )

        self.client.force_authenticate(user=self.staff)
        url = '/api/maintenance-logs/?log_type=damage'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for log in response.data:
            self.assertEqual(log['log_type'], 'damage')


class DashboardStatsViewTest(APITestCase):
    """Test cases for dashboard statistics"""

    def setUp(self):
        self.client = APIClient()
        self.student = User.objects.create_user(
            username='student',
            password='pass123',
            role='student'
        )
        self.staff = User.objects.create_user(
            username='staff',
            password='pass123',
            role='staff'
        )
        self.equipment = Equipment.objects.create(
            name='Camera',
            category='camera',
            quantity=5,
            available_quantity=3
        )

    def test_dashboard_stats_as_student(self):
        """Test dashboard stats for student"""
        BorrowRequest.objects.create(
            user=self.student,
            equipment=self.equipment,
            quantity=1,
            status='pending',
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=3)
        )

        self.client.force_authenticate(user=self.student)
        url = '/api/dashboard/stats/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('my_requests', response.data)
        self.assertIn('my_pending', response.data)
        self.assertIn('total_equipment', response.data)

    def test_dashboard_stats_as_staff(self):
        """Test dashboard stats for staff"""
        BorrowRequest.objects.create(
            user=self.student,
            equipment=self.equipment,
            quantity=1,
            status='pending',
            borrow_from=date.today() + timedelta(days=1),
            borrow_to=date.today() + timedelta(days=3)
        )

        self.client.force_authenticate(user=self.staff)
        url = '/api/dashboard/stats/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('pending_requests', response.data)
        self.assertIn('approved_requests', response.data)
        self.assertIn('total_equipment', response.data)

    def test_dashboard_stats_unauthenticated(self):
        """Test dashboard stats without authentication"""
        url = '/api/dashboard/stats/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# ==================== PERMISSION TESTS ====================

class PermissionTest(TestCase):
    """Test cases for custom permissions"""

    def setUp(self):
        self.admin = User.objects.create_user(
            username='admin',
            password='pass123',
            role='admin'
        )
        self.staff = User.objects.create_user(
            username='staff',
            password='pass123',
            role='staff'
        )
        self.student = User.objects.create_user(
            username='student',
            password='pass123',
            role='student'
        )

    def test_is_admin_permission(self):
        """Test IsAdmin permission"""
        from .permissions import IsAdmin
        from rest_framework.test import APIRequestFactory
        from rest_framework.request import Request

        factory = APIRequestFactory()
        request = factory.get('/')
        permission = IsAdmin()

        # Test with admin
        request = Request(request)
        request.user = self.admin
        self.assertTrue(permission.has_permission(request, None))

        # Test with staff
        request.user = self.staff
        self.assertFalse(permission.has_permission(request, None))

        # Test with student
        request.user = self.student
        self.assertFalse(permission.has_permission(request, None))

    def test_is_staff_or_admin_permission(self):
        """Test IsStaffOrAdmin permission"""
        from .permissions import IsStaffOrAdmin
        from rest_framework.test import APIRequestFactory
        from rest_framework.request import Request

        factory = APIRequestFactory()
        request = factory.get('/')
        permission = IsStaffOrAdmin()

        # Test with admin
        request = Request(request)
        request.user = self.admin
        self.assertTrue(permission.has_permission(request, None))

        # Test with staff
        request.user = self.staff
        self.assertTrue(permission.has_permission(request, None))

        # Test with student
        request.user = self.student
        self.assertFalse(permission.has_permission(request, None))


# ==================== INTEGRATION TESTS ====================

class BorrowingWorkflowIntegrationTest(APITestCase):
    """Integration test for complete borrowing workflow"""

    def setUp(self):
        self.client = APIClient()
        self.student = User.objects.create_user(
            username='student',
            password='pass123',
            role='student'
        )
        self.staff = User.objects.create_user(
            username='staff',
            password='pass123',
            role='staff'
        )
        self.equipment = Equipment.objects.create(
            name='Camera',
            category='camera',
            quantity=5,
            available_quantity=5
        )

    def test_complete_borrowing_workflow(self):
        """Test complete workflow: request -> approve -> issue -> return"""

        # 1. Student creates request
        self.client.force_authenticate(user=self.student)
        url = '/api/borrow-requests/'
        data = {
            'equipment': self.equipment.id,
            'quantity': 2,
            'borrow_from': str(date.today() + timedelta(days=1)),
            'borrow_to': str(date.today() + timedelta(days=5)),
            'purpose': 'School project'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Get the created request from database
        borrow_request = BorrowRequest.objects.get(user=self.student)
        request_id = borrow_request.id

        # 2. Staff approves request
        self.client.force_authenticate(user=self.staff)
        url = f'/api/borrow-requests/{request_id}/approve/'
        response = self.client.post(url, {'notes': 'Approved'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'approved')

        # 3. Staff issues equipment
        url = f'/api/borrow-requests/{request_id}/issue/'
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'issued')

        # Verify equipment quantity decreased
        self.equipment.refresh_from_db()
        self.assertEqual(self.equipment.available_quantity, 3)

        # 4. Staff marks as returned
        url = f'/api/borrow-requests/{request_id}/mark_returned/'
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'returned')

        # Verify equipment quantity increased back
        self.equipment.refresh_from_db()
        self.assertEqual(self.equipment.available_quantity, 5)

    def test_overlapping_requests_workflow(self):
        """Test workflow with overlapping requests"""

        # Create and approve first request
        self.client.force_authenticate(user=self.student)
        url = '/api/borrow-requests/'
        data = {
            'equipment': self.equipment.id,
            'quantity': 3,
            'borrow_from': str(date.today() + timedelta(days=1)),
            'borrow_to': str(date.today() + timedelta(days=5)),
            'purpose': 'Project 1'
        }
        response = self.client.post(url, data, format='json')
        # Get the created request from database
        borrow_request = BorrowRequest.objects.get(user=self.student, purpose='Project 1')
        request1_id = borrow_request.id

        self.client.force_authenticate(user=self.staff)
        url = f'/api/borrow-requests/{request1_id}/approve/'
        self.client.post(url, {}, format='json')

        # Try to create overlapping request that would exceed capacity
        self.client.force_authenticate(user=self.student)
        url = '/api/borrow-requests/'
        data = {
            'equipment': self.equipment.id,
            'quantity': 3,  # 3 + 3 = 6 > 5 total
            'borrow_from': str(date.today() + timedelta(days=2)),
            'borrow_to': str(date.today() + timedelta(days=4)),
            'purpose': 'Project 2'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
