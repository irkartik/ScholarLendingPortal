# Equipment Lending System - Backend

Django REST Framework backend for the Equipment Lending System.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python3 -m venv venv
```

3. Activate the virtual environment:
   - On Linux/Mac:
   ```bash
   source venv/bin/activate
   ```
   - On Windows:
   ```bash
   venv\Scripts\activate
   ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Equipment
- `GET /api/equipment/` - List all equipment
- `POST /api/equipment/` - Create new equipment
- `GET /api/equipment/{id}/` - Get equipment details
- `PUT /api/equipment/{id}/` - Update equipment
- `DELETE /api/equipment/{id}/` - Delete equipment
- `GET /api/equipment/{id}/available/` - Get available quantity

### Lending Records
- `GET /api/lending-records/` - List all lending records
- `POST /api/lending-records/` - Create new lending record
- `GET /api/lending-records/{id}/` - Get lending record details
- `PUT /api/lending-records/{id}/` - Update lending record
- `DELETE /api/lending-records/{id}/` - Delete lending record
- `POST /api/lending-records/{id}/approve/` - Approve a lending request
- `POST /api/lending-records/{id}/return_equipment/` - Mark equipment as returned

### Admin Panel
Access the admin panel at `http://localhost:8000/admin/`

## Project Structure

```
backend/
├── config/              # Project configuration
│   ├── settings.py      # Django settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── equipment/           # Equipment app
│   ├── models.py        # Database models
│   ├── views.py         # API views
│   ├── serializers.py   # DRF serializers
│   ├── urls.py          # App URL configuration
│   └── admin.py         # Admin configuration
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

## Models

### Equipment
- name: Equipment name
- description: Detailed description
- category: Equipment category
- quantity_available: Available quantity
- quantity_total: Total quantity
- is_available: Availability status

### LendingRecord
- equipment: Foreign key to Equipment
- user: Foreign key to User
- quantity: Quantity borrowed
- status: Record status (pending, approved, borrowed, returned, cancelled)
- borrow_date: Date borrowed
- due_date: Due date
- return_date: Date returned
- notes: Additional notes
