# ScholarLendingPortal

Equipment Lending System for educational institutions. A full-stack application with React frontend and Django backend.

## Project Structure

```
ScholarLendingPortal/
├── backend/            # Django REST API
│   ├── config/         # Django project settings
│   ├── equipment/      # Equipment lending app
│   ├── manage.py
│   ├── requirements.txt
│   └── README.md
├── frontend/           # React application
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── README.md
└── README.md           # This file
```

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn
- pip

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser (optional):
```bash
python manage.py createsuperuser
```

6. Start the backend server:
```bash
python manage.py runserver
```

Backend will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create environment file:
```bash
cp .env.example .env
```

4. Start the development server:
```bash
npm run dev
```

Frontend will be available at `http://localhost:5173`

## Features

### Current Features
- Equipment inventory management
- Lending record tracking
- RESTful API endpoints
- Responsive UI
- Status tracking for equipment and loans

### Equipment Management
- Add, view, update, and delete equipment
- Track available quantities
- Categorize equipment
- View equipment details

### Lending Records
- Create lending requests
- Track borrowing status (pending, approved, borrowed, returned, cancelled)
- View lending history
- Approve and return equipment

## Technology Stack

### Backend
- **Django 5.2.7** - Web framework
- **Django REST Framework** - API framework
- **django-cors-headers** - CORS support
- **SQLite** - Database (default, can be changed)

### Frontend
- **React 18** - UI library
- **Vite** - Build tool
- **React Router** - Routing
- **Axios** - HTTP client

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
- `GET /api/lending-records/{id}/` - Get record details
- `PUT /api/lending-records/{id}/` - Update record
- `DELETE /api/lending-records/{id}/` - Delete record
- `POST /api/lending-records/{id}/approve/` - Approve a request
- `POST /api/lending-records/{id}/return_equipment/` - Mark as returned

### Admin Panel
Access at `http://localhost:8000/admin/`

## Development

### Running Both Servers

For development, run both backend and frontend servers simultaneously in separate terminals:

**Terminal 1 (Backend):**
```bash
cd backend
source venv/bin/activate
python manage.py runserver
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm run dev
```

### Making Changes

**Backend Changes:**
- Models are in `backend/equipment/models.py`
- Views in `backend/equipment/views.py`
- Serializers in `backend/equipment/serializers.py`
- URLs in `backend/equipment/urls.py`

After model changes, run:
```bash
python manage.py makemigrations
python manage.py migrate
```

**Frontend Changes:**
- Components in `frontend/src/components/`
- Pages in `frontend/src/pages/`
- API calls in `frontend/src/services/api.js`
- Routing in `frontend/src/App.jsx`

## Extending the System

This boilerplate can be extended to add:

- **Authentication & Authorization**
  - User login/logout
  - Role-based permissions
  - JWT tokens

- **Advanced Features**
  - Email notifications
  - SMS reminders
  - Equipment reservation system
  - QR code scanning
  - Barcode support
  - File uploads (equipment images, documents)
  - Advanced search and filtering
  - Export to CSV/PDF
  - Analytics dashboard

- **Enhanced UI**
  - User profiles
  - Equipment images
  - Calendar view for bookings
  - Real-time updates with WebSockets
  - Mobile responsive improvements

- **Database**
  - Switch to PostgreSQL for production
  - Add caching with Redis
  - Implement full-text search

## Deployment

### Backend
- Use production WSGI server (gunicorn, uWSGI)
- Configure PostgreSQL database
- Set up static file serving
- Configure environment variables
- Set DEBUG=False

### Frontend
- Build production bundle: `npm run build`
- Deploy dist folder to static hosting
- Configure API URL for production

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available for educational purposes.

## Support

For issues and questions:
- Check the README files in backend/ and frontend/ directories
- Review Django and React documentation
- Open an issue on the repository
