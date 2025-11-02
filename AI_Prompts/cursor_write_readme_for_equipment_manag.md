# Write README for equipment management system
_Exported on 02/11/2025 at 22:38:21 GMT+5:30 from Cursor (1.7.52)_

---

**User**

You're an expert Fullstack developer having experience with Django for backend and React for frontend. This project is a School's Equipment Management System which is used to keep track of and handle the borowing lifecycle of each equipments. 

However, the current project lacks API documentation and project description. I would like you to write a README file on the root level of this project which explains the following : 

1. Basic project description including user types and their functionality in the system
2. Techstack being used 
3. Quickstart on how to get started locally for both backend and frontend
3. API Documentation of backend


---

**Cursor**

I'll help you create a comprehensive README file for the School Equipment Management System. Let me first explore the project structure to understand the system better.

Now I'll create a comprehensive README file for the project with all the required information.

```markdown
# Scholar Lending Portal

A comprehensive School Equipment Management System designed to streamline the borrowing lifecycle of school equipment. This web application enables students to request equipment, while staff and administrators can efficiently manage inventory, approvals, and maintenance.

## 📋 Table of Contents

- [Overview](#overview)
- [User Types & Functionalities](#user-types--functionalities)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [API Documentation](#api-documentation)
- [Features](#features)

## Overview

The Scholar Lending Portal is a full-stack web application that facilitates the management of school equipment lending operations. It provides a role-based access control system with three distinct user types, each with specific permissions and capabilities.

### Key Features

- **Equipment Management**: Track and manage various types of equipment (sports, lab, cameras, musical instruments, etc.)
- **Borrow Request Workflow**: Complete lifecycle management from request creation to equipment return
- **Maintenance Tracking**: Log and monitor equipment damage, repairs, and inspections
- **Real-time Availability**: Automatic tracking of equipment availability based on approved bookings
- **Role-based Access Control**: Different permissions for students, staff, and administrators
- **Dashboard Analytics**: Statistics and insights for better decision-making

## User Types & Functionalities

### 👨‍🎓 Student
Students have access to browse and borrow equipment:
- Browse available equipment catalog
- Search and filter equipment by category, condition, and availability
- Create borrow requests with date range and purpose
- View their own borrow request history
- Track status of pending, approved, and issued requests
- View dashboard with personal statistics

### 👨‍💼 Staff
Staff members can manage the borrowing workflow:
- All student functionalities
- View all borrow requests from students
- Approve or reject pending borrow requests
- Issue equipment to students (mark as issued)
- Process equipment returns
- Create and view maintenance logs
- View dashboard with system-wide statistics
- Filter and search requests by status, user, and equipment

### 👨‍💻 Admin
Administrators have full system access:
- All staff functionalities
- Create, update, and delete equipment
- Manage equipment inventory and availability
- Update equipment condition and quantities
- Full access to all system features
- Comprehensive dashboard analytics

## Tech Stack

### Backend
- **Framework**: Django 4.2.7
- **API**: Django REST Framework 3.14.0
- **Authentication**: JWT (djangorestframework-simplejwt 5.3.0)
- **Database**: SQLite (Development)
- **CORS**: django-cors-headers 4.3.0
- **Configuration**: python-decouple 3.8

### Frontend
- **Framework**: React 19.2.0
- **Routing**: React Router DOM 7.9.5
- **Build Tool**: React Scripts 5.0.1
- **Testing**: React Testing Library 16.3.0

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- **Python**: 3.9 or higher
- **Node.js**: 14.x or higher
- **npm**: 6.x or higher
- **pip**: Latest version

### Backend Setup

1. **Navigate to the backend directory**
   ```bash
   cd backend/ScholarLendingPortal
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional but recommended)
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account.

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

   The backend server will be running at `http://127.0.0.1:8000/`

7. **Access the Admin Panel** (optional)
   Visit `http://127.0.0.1:8000/admin/` and login with your superuser credentials.

### Frontend Setup

1. **Navigate to the frontend directory**
   ```bash
   cd frontend/scholarlendingportal
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm start
   ```

   The frontend application will open automatically at `http://localhost:3000/`

4. **Build for production** (optional)
   ```bash
   npm run build
   ```

## API Documentation

Base URL: `http://127.0.0.1:8000/api/`

### Authentication Endpoints

#### Register User
- **URL**: `/api/auth/register/`
- **Method**: `POST`
- **Authentication**: Not required
- **Request Body**:
  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string",
    "first_name": "string",
    "last_name": "string",
    "role": "student|staff|admin",
    "phone_number": "string"
  }
  ```
- **Response** (201 Created):
  ```json
  {
    "user": {
      "id": 1,
      "username": "string",
      "email": "string",
      "first_name": "string",
      "last_name": "string",
      "role": "student",
      "phone_number": "string"
    },
    "refresh": "jwt_refresh_token",
    "access": "jwt_access_token"
  }
  ```

#### Login
- **URL**: `/api/auth/login/`
- **Method**: `POST`
- **Authentication**: Not required
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response** (200 OK):
  ```json
  {
    "user": {
      "id": 1,
      "username": "string",
      "email": "string",
      "role": "student"
    },
    "refresh": "jwt_refresh_token",
    "access": "jwt_access_token"
  }
  ```

#### Get Current User
- **URL**: `/api/auth/user/`
- **Method**: `GET`
- **Authentication**: Required (JWT)
- **Response** (200 OK):
  ```json
  {
    "id": 1,
    "username": "string",
    "email": "string",
    "first_name": "string",
    "last_name": "string",
    "role": "student",
    "phone_number": "string"
  }
  ```

### Equipment Endpoints

#### List Equipment
- **URL**: `/api/equipment/`
- **Method**: `GET`
- **Authentication**: Required
- **Query Parameters**:
  - `search` (string): Search by equipment name
  - `category` (string): Filter by category (sports, lab, camera, musical, project, other)
  - `condition` (string): Filter by condition (excellent, good, fair, poor)
  - `available` (boolean): Filter by availability (true/false)
- **Response** (200 OK):
  ```json
  [
    {
      "id": 1,
      "name": "string",
      "category": "sports",
      "description": "string",
      "condition": "good",
      "quantity": 10,
      "available_quantity": 8,
      "is_available": true,
      "created_at": "2024-01-01T00:00:00Z",
      "updated_at": "2024-01-01T00:00:00Z"
    }
  ]
  ```

#### Get Equipment Details
- **URL**: `/api/equipment/{id}/`
- **Method**: `GET`
- **Authentication**: Required
- **Response** (200 OK): Same as single equipment object above

#### Create Equipment
- **URL**: `/api/equipment/`
- **Method**: `POST`
- **Authentication**: Required (Admin only)
- **Request Body**:
  ```json
  {
    "name": "string",
    "category": "sports|lab|camera|musical|project|other",
    "description": "string",
    "condition": "excellent|good|fair|poor",
    "quantity": 10,
    "available_quantity": 10
  }
  ```
- **Response** (201 Created): Equipment object

#### Update Equipment
- **URL**: `/api/equipment/{id}/`
- **Method**: `PUT` or `PATCH`
- **Authentication**: Required (Admin only)
- **Request Body**: Same as create (all fields for PUT, partial for PATCH)
- **Response** (200 OK): Updated equipment object

#### Delete Equipment
- **URL**: `/api/equipment/{id}/`
- **Method**: `DELETE`
- **Authentication**: Required (Admin only)
- **Response** (204 No Content)

#### Get Equipment Categories
- **URL**: `/api/equipment/categories/`
- **Method**: `GET`
- **Authentication**: Required
- **Response** (200 OK):
  ```json
  [
    {
      "value": "sports",
      "label": "Sports Equipment"
    }
  ]
  ```

#### Get Equipment Conditions
- **URL**: `/api/equipment/conditions/`
- **Method**: `GET`
- **Authentication**: Required
- **Response** (200 OK):
  ```json
  [
    {
      "value": "excellent",
      "label": "Excellent"
    }
  ]
  ```

### Borrow Request Endpoints

#### List Borrow Requests
- **URL**: `/api/borrow-requests/`
- **Method**: `GET`
- **Authentication**: Required
- **Query Parameters**:
  - `status` (string): Filter by status (pending, approved, rejected, issued, returned)
  - `user` (int): Filter by user ID (staff/admin only)
  - `equipment` (int): Filter by equipment ID
- **Response** (200 OK):
  ```json
  [
    {
      "id": 1,
      "user": 1,
      "equipment": 1,
      "quantity": 1,
      "status": "pending",
      "request_date": "2024-01-01T00:00:00Z",
      "borrow_from": "2024-01-10",
      "borrow_to": "2024-01-15",
      "approved_by": null,
      "approved_date": null,
      "issued_date": null,
      "returned_date": null,
      "purpose": "string",
      "rejection_reason": "",
      "notes": "",
      "user_details": {...},
      "equipment_details": {...},
      "approved_by_details": null
    }
  ]
  ```

#### Create Borrow Request
- **URL**: `/api/borrow-requests/`
- **Method**: `POST`
- **Authentication**: Required
- **Request Body**:
  ```json
  {
    "equipment": 1,
    "quantity": 1,
    "borrow_from": "2024-01-10",
    "borrow_to": "2024-01-15",
    "purpose": "string"
  }
  ```
- **Response** (201 Created): Borrow request object

#### Get Borrow Request Details
- **URL**: `/api/borrow-requests/{id}/`
- **Method**: `GET`
- **Authentication**: Required
- **Response** (200 OK): Borrow request object

#### Get My Requests
- **URL**: `/api/borrow-requests/my_requests/`
- **Method**: `GET`
- **Authentication**: Required
- **Response** (200 OK): Array of current user's borrow requests

#### Get Pending Approvals
- **URL**: `/api/borrow-requests/pending_approvals/`
- **Method**: `GET`
- **Authentication**: Required (Staff/Admin only)
- **Response** (200 OK): Array of pending borrow requests

#### Approve Borrow Request
- **URL**: `/api/borrow-requests/{id}/approve/`
- **Method**: `POST`
- **Authentication**: Required (Staff/Admin only)
- **Request Body**:
  ```json
  {
    "notes": "string (optional)"
  }
  ```
- **Response** (200 OK): Updated borrow request object
- **Error** (400): If request is not pending or equipment unavailable

#### Reject Borrow Request
- **URL**: `/api/borrow-requests/{id}/reject/`
- **Method**: `POST`
- **Authentication**: Required (Staff/Admin only)
- **Request Body**:
  ```json
  {
    "rejection_reason": "string (optional)",
    "notes": "string (optional)"
  }
  ```
- **Response** (200 OK): Updated borrow request object
- **Error** (400): If request is not pending

#### Issue Equipment
- **URL**: `/api/borrow-requests/{id}/issue/`
- **Method**: `POST`
- **Authentication**: Required (Staff/Admin only)
- **Response** (200 OK): Updated borrow request object
- **Error** (400): If request is not approved or equipment unavailable

#### Mark as Returned
- **URL**: `/api/borrow-requests/{id}/mark_returned/`
- **Method**: `POST`
- **Authentication**: Required (Staff/Admin only)
- **Response** (200 OK): Updated borrow request object
- **Error** (400): If request is not issued

### Maintenance Log Endpoints

#### List Maintenance Logs
- **URL**: `/api/maintenance-logs/`
- **Method**: `GET`
- **Authentication**: Required
- **Query Parameters**:
  - `equipment` (int): Filter by equipment ID
  - `log_type` (string): Filter by log type (damage, repair, inspection)
- **Response** (200 OK):
  ```json
  [
    {
      "id": 1,
      "equipment": 1,
      "log_type": "damage",
      "description": "string",
      "reported_by": 1,
      "reported_date": "2024-01-01T00:00:00Z",
      "cost": "100.00",
      "equipment_details": {...},
      "reported_by_details": {...}
    }
  ]
  ```

#### Create Maintenance Log
- **URL**: `/api/maintenance-logs/`
- **Method**: `POST`
- **Authentication**: Required
- **Request Body**:
  ```json
  {
    "equipment": 1,
    "log_type": "damage|repair|inspection",
    "description": "string",
    "cost": "100.00"
  }
  ```
- **Response** (201 Created): Maintenance log object

#### Get Maintenance Log Details
- **URL**: `/api/maintenance-logs/{id}/`
- **Method**: `GET`
- **Authentication**: Required
- **Response** (200 OK): Maintenance log object

#### Update Maintenance Log
- **URL**: `/api/maintenance-logs/{id}/`
- **Method**: `PUT` or `PATCH`
- **Authentication**: Required
- **Request Body**: Same as create
- **Response** (200 OK): Updated maintenance log object

#### Delete Maintenance Log
- **URL**: `/api/maintenance-logs/{id}/`
- **Method**: `DELETE`
- **Authentication**: Required
- **Response** (204 No Content)

### Dashboard Endpoints

#### Get Dashboard Statistics
- **URL**: `/api/dashboard/stats/`
- **Method**: `GET`
- **Authentication**: Required
- **Response for Students** (200 OK):
  ```json
  {
    "total_equipment": 50,
    "available_equipment": 35,
    "my_requests": 10,
    "my_pending": 2,
    "my_issued": 1
  }
  ```
- **Response for Staff/Admin** (200 OK):
  ```json
  {
    "total_equipment": 50,
    "available_equipment": 35,
    "pending_requests": 15,
    "approved_requests": 10,
    "issued_requests": 8
  }
  ```

## Features

### Equipment Categories
- **Sports Equipment**: Balls, nets, protective gear, etc.
- **Lab Equipment**: Microscopes, measuring instruments, etc.
- **Camera & Photography**: Cameras, lenses, lighting equipment
- **Musical Instruments**: Guitars, keyboards, percussion
- **Project Materials**: Tools, supplies for projects
- **Other**: Miscellaneous equipment

### Equipment Conditions
- **Excellent**: Brand new or like-new condition
- **Good**: Minor wear, fully functional
- **Fair**: Visible wear but functional
- **Poor**: Significant wear, may need maintenance

### Request Status Flow
1. **Pending**: Initial state when request is created
2. **Approved**: Staff/Admin has approved the request
3. **Rejected**: Staff/Admin has rejected the request
4. **Issued**: Equipment has been physically given to the student
5. **Returned**: Equipment has been returned by the student

### Authentication
All protected endpoints require JWT authentication. Include the access token in the Authorization header:
```
Authorization: Bearer <access_token>
```

To refresh the access token, use the refresh token with the appropriate JWT refresh endpoint (implementation depends on your frontend setup).

## Development Notes

### Database
The application uses SQLite for development. For production, consider migrating to PostgreSQL or MySQL.

### CORS Configuration
The backend is configured to accept requests from:
- `http://localhost:3000`
- `http://127.0.0.1:3000`

Update `CORS_ALLOWED_ORIGINS` in `settings.py` for production deployments.

### Environment Variables
Consider using environment variables for sensitive configuration in production:
- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- `DATABASE_URL`

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is created for educational purposes.

## Support

For issues, questions, or contributions, please open an issue in the repository.

---

**Note**: This is a development setup. For production deployment, ensure you configure proper security settings, use a production-grade database, set up proper environment variables, and follow Django deployment best practices.

```

Perfect! I've created a comprehensive README.md file for your Scholar Lending Portal project. The documentation includes:

## What's Included:

### 1. **Project Description**
   - Overview of the School Equipment Management System
   - Key features and capabilities
   - Complete breakdown of all three user types (Student, Staff, Admin) with their specific functionalities

### 2. **Tech Stack**
   - **Backend**: Django 4.2.7, Django REST Framework, JWT Authentication, SQLite
   - **Frontend**: React 19.2.0, React Router DOM 7.9.5
   - All dependencies listed with versions

### 3. **Quickstart Guides**
   - **Backend Setup**: Complete step-by-step instructions including virtual environment setup, dependency installation, database migrations, and server startup
   - **Frontend Setup**: Instructions for installing dependencies and running the development server

### 4. **Complete API Documentation**
   - **Authentication APIs**: Register, Login, Get Current User
   - **Equipment APIs**: CRUD operations, filtering, categories, conditions
   - **Borrow Request APIs**: Create requests, approve/reject/issue/return workflow, filtering
   - **Maintenance Log APIs**: Create, read, update, delete logs
   - **Dashboard APIs**: Statistics for different user roles
   - Each endpoint includes:
     - URL and HTTP method
     - Authentication requirements
     - Request/response body examples
     - Query parameters where applicable
     - Error responses

### 5. **Additional Information**
   - Equipment categories and conditions
   - Request status flow
   - JWT authentication instructions
   - Development notes and best practices
   - CORS configuration details

The README is now located at the root of your project and provides everything needed for developers to understand, set up, and work with the Scholar Lending Portal! 📚✨

