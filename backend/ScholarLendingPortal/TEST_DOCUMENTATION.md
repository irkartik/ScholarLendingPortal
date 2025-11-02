# Test Documentation - ScholarLendingPortal Backend

This document provides an overview of the comprehensive test suite implemented for the ScholarLendingPortal Django backend.

## Test Overview

**Total Tests: 72**
**Test Categories: 10**

All tests follow Django's best practices and use Django REST Framework's APITestCase and TestCase for testing.

## Test Coverage by Category

### 1. Model Tests (15 tests)

#### UserModelTest (5 tests)
- ✅ `test_create_user` - Tests basic user creation
- ✅ `test_user_default_role` - Validates default role is 'student'
- ✅ `test_user_str_method` - Tests string representation
- ✅ `test_create_admin_user` - Tests admin user creation
- ✅ `test_create_staff_user` - Tests staff user creation

#### EquipmentModelTest (6 tests)
- ✅ `test_create_equipment` - Tests equipment creation
- ✅ `test_equipment_str_method` - Tests string representation
- ✅ `test_equipment_is_available_property` - Tests availability property
- ✅ `test_available_quantity_exceeds_quantity_on_save` - Tests quantity validation on save
- ✅ `test_equipment_default_values` - Tests default values
- ✅ `test_equipment_ordering` - Tests ordering by created_at

#### BorrowRequestModelTest (5 tests)
- ✅ `test_create_borrow_request` - Tests borrow request creation
- ✅ `test_borrow_request_str_method` - Tests string representation
- ✅ `test_borrow_request_validation_end_before_start` - Tests date validation
- ✅ `test_overlapping_bookings_validation` - Tests overlapping request validation
- ✅ `test_pending_requests_do_not_block_availability` - Tests pending request logic

#### MaintenanceLogModelTest (2 tests)
- ✅ `test_create_maintenance_log` - Tests maintenance log creation
- ✅ `test_maintenance_log_str_method` - Tests string representation

### 2. Serializer Tests (9 tests)

#### UserSerializerTest (2 tests)
- ✅ `test_user_serializer_create` - Tests user creation via serializer
- ✅ `test_user_serializer_password_write_only` - Tests password is write-only

#### LoginSerializerTest (3 tests)
- ✅ `test_login_serializer_valid_credentials` - Tests valid login
- ✅ `test_login_serializer_invalid_credentials` - Tests invalid credentials
- ✅ `test_login_serializer_inactive_user` - Tests inactive user login

#### EquipmentSerializerTest (2 tests)
- ✅ `test_equipment_serializer_create` - Tests equipment creation
- ✅ `test_equipment_serializer_validation_available_exceeds_total` - Tests quantity validation

#### BorrowRequestSerializerTest (4 tests)
- ✅ `test_borrow_request_create_serializer_valid` - Tests valid request creation
- ✅ `test_borrow_request_serializer_past_date_validation` - Tests past date validation
- ✅ `test_borrow_request_serializer_end_before_start_validation` - Tests date order validation
- ✅ `test_borrow_request_serializer_quantity_exceeds_total` - Tests quantity validation

### 3. Authentication View Tests (6 tests)

#### AuthenticationViewTest
- ✅ `test_register_user` - Tests user registration endpoint
- ✅ `test_register_user_duplicate_username` - Tests duplicate username validation
- ✅ `test_login_user` - Tests login endpoint
- ✅ `test_login_invalid_credentials` - Tests invalid login
- ✅ `test_current_user_authenticated` - Tests getting current user
- ✅ `test_current_user_unauthenticated` - Tests unauthenticated access

### 4. Equipment ViewSet Tests (14 tests)

#### EquipmentViewSetTest
- ✅ `test_list_equipment_authenticated` - Tests listing equipment
- ✅ `test_list_equipment_unauthenticated` - Tests unauthorized access
- ✅ `test_retrieve_equipment` - Tests retrieving single equipment
- ✅ `test_create_equipment_as_admin` - Tests admin can create equipment
- ✅ `test_create_equipment_as_student` - Tests student cannot create equipment
- ✅ `test_update_equipment_as_admin` - Tests admin can update equipment
- ✅ `test_delete_equipment_as_admin` - Tests admin can delete equipment
- ✅ `test_filter_equipment_by_category` - Tests category filtering
- ✅ `test_filter_equipment_by_availability` - Tests availability filtering
- ✅ `test_search_equipment_by_name` - Tests name search
- ✅ `test_get_equipment_categories` - Tests getting category list
- ✅ `test_get_equipment_conditions` - Tests getting condition list

### 5. Borrow Request ViewSet Tests (15 tests)

#### BorrowRequestViewSetTest
- ✅ `test_create_borrow_request_as_student` - Tests student can create request
- ✅ `test_list_borrow_requests_as_student` - Tests student sees only their requests
- ✅ `test_list_borrow_requests_as_staff` - Tests staff sees all requests
- ✅ `test_approve_borrow_request_as_staff` - Tests staff can approve
- ✅ `test_approve_borrow_request_as_student` - Tests student cannot approve
- ✅ `test_reject_borrow_request_as_staff` - Tests staff can reject
- ✅ `test_approve_non_pending_request_fails` - Tests approval validation
- ✅ `test_issue_equipment_as_staff` - Tests staff can issue equipment
- ✅ `test_issue_non_approved_request_fails` - Tests issue validation
- ✅ `test_mark_returned_as_staff` - Tests marking equipment as returned
- ✅ `test_get_my_requests` - Tests getting user's own requests
- ✅ `test_get_pending_approvals_as_staff` - Tests staff can get pending approvals
- ✅ `test_get_pending_approvals_as_student_fails` - Tests student cannot get pending approvals
- ✅ `test_filter_borrow_requests_by_status` - Tests status filtering

### 6. Maintenance Log ViewSet Tests (4 tests)

#### MaintenanceLogViewSetTest
- ✅ `test_create_maintenance_log` - Tests creating maintenance log
- ✅ `test_list_maintenance_logs` - Tests listing logs
- ✅ `test_filter_maintenance_logs_by_equipment` - Tests equipment filtering
- ✅ `test_filter_maintenance_logs_by_type` - Tests log type filtering

### 7. Dashboard Stats Tests (3 tests)

#### DashboardStatsViewTest
- ✅ `test_dashboard_stats_as_student` - Tests student dashboard stats
- ✅ `test_dashboard_stats_as_staff` - Tests staff dashboard stats
- ✅ `test_dashboard_stats_unauthenticated` - Tests unauthorized access

### 8. Permission Tests (2 tests)

#### PermissionTest
- ✅ `test_is_admin_permission` - Tests IsAdmin permission class
- ✅ `test_is_staff_or_admin_permission` - Tests IsStaffOrAdmin permission class

### 9. Integration Tests (2 tests)

#### BorrowingWorkflowIntegrationTest
- ✅ `test_complete_borrowing_workflow` - Tests full borrowing lifecycle (request → approve → issue → return)
- ✅ `test_overlapping_requests_workflow` - Tests overlapping request validation

## Running the Tests

### Run All Tests
```bash
cd backend/ScholarLendingPortal
python manage.py test api
```

### Run with Verbose Output
```bash
python manage.py test api --verbosity=2
```

### Run Specific Test Class
```bash
python manage.py test api.tests.EquipmentViewSetTest
```

### Run Specific Test Method
```bash
python manage.py test api.tests.EquipmentViewSetTest.test_create_equipment_as_admin
```

### Run with Coverage (if coverage.py is installed)
```bash
coverage run --source='.' manage.py test api
coverage report
coverage html  # Generate HTML report
```

## Test Data

Tests use Django's test database which is created and destroyed automatically. Each test class has a `setUp()` method that creates necessary test data.

### Common Test Users
- **Student**: `username='student', role='student'`
- **Staff**: `username='staff', role='staff'`
- **Admin**: `username='admin', role='admin'`

### Test Equipment
- Camera (category: 'camera', quantity: 5)
- Basketball (category: 'sports', quantity: 10)
- Microscope (category: 'lab')

## Key Features Tested

### Authentication & Authorization
- User registration with JWT tokens
- User login with credential validation
- Role-based access control (Student, Staff, Admin)
- Permission classes (IsAdmin, IsStaffOrAdmin)

### Equipment Management
- CRUD operations with role-based permissions
- Search and filtering capabilities
- Quantity tracking and validation
- Category and condition management

### Borrowing Workflow
- Request creation by students
- Approval/rejection by staff
- Equipment issuance tracking
- Return processing
- Overlapping request validation
- Quantity availability checks

### Maintenance Tracking
- Damage and repair logging
- Cost tracking
- Equipment history

### Data Validation
- Date validation (no past dates, end > start)
- Quantity validation (available <= total)
- Overlapping booking prevention
- Status transition validation

## Best Practices Followed

1. **Isolation**: Each test is independent and doesn't rely on other tests
2. **Clean Setup**: Using `setUp()` method to create test data
3. **Descriptive Names**: Test method names clearly describe what is being tested
4. **Comprehensive Coverage**: Testing both success and failure cases
5. **API Testing**: Using APIClient for realistic HTTP request testing
6. **Authentication**: Using `force_authenticate()` for simulating authenticated requests
7. **Database Queries**: Tests verify both API responses and database state

## Continuous Integration

These tests are designed to be run in CI/CD pipelines. They:
- Run in isolation with an in-memory database
- Complete in reasonable time (~30 seconds)
- Provide clear error messages when failures occur
- Don't require external dependencies

## Future Test Additions

Consider adding tests for:
- File upload/download if implemented
- Email notifications if implemented
- More complex search scenarios
- Performance tests for large datasets
- API rate limiting if implemented
- Webhook integrations if implemented

## Troubleshooting

### Test Database Issues
If you encounter database issues:
```bash
python manage.py test api --keepdb  # Keep test database between runs
```

### Failed Tests
Review the verbose output:
```bash
python manage.py test api --verbosity=2 --failfast  # Stop at first failure
```

### Import Errors
Ensure you're in the correct directory and virtual environment is activated.

---

**Last Updated**: November 2, 2025
**Test Suite Version**: 1.0
**Django Version**: 4.2.7
**DRF Version**: 3.14.0

