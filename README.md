# Scholar Lending Portal

School Equipment Lending Portal to manage borrowing, approvals, issuance and returns of shared equipment (sports kits, lab equipment, cameras, instruments, project materials).

## Summary

A full-stack web application:

- Django REST backend (with JWT auth)
- React frontend (responsive UI)
- Role-based access: student, staff, admin
- Core flows: request, approve/issue, return, inventory management, search/filter

## Core Features

- User authentication & roles (signup/login, token-based)
- Equipment management (CRUD by admin): name, category, condition, quantity, availability
- Borrow/return requests (students request; staff/admin approve/reject)
- Prevent overlapping bookings for same item
- Equipment dashboard with search/filter by category and availability
- Basic responsive React UI with navigation

## Tech Stack

- Backend: Python, Django 4.2, Django REST Framework, djangorestframework-simplejwt, django-cors-headers
- Frontend: React (JS/TS), fetch/axios
- DB: SQLite (development); configurable to PostgreSQL
- Dev OS: Windows (commands in README assume Windows)

## Repository structure

- backend/
  - manage.py
  - requirements.txt
  - ScholarLendingPortal/ (Django project)
  - api/ (app: models, serializers, views, urls)
- frontend/
  - package.json
  - src/ (React app)
- README.md
- docker-compose.yml (optional)

## Quickstart — Backend (Windows)

1. Open terminal (PowerShell or CMD) at `backend`:
   - PowerShell example:
     - python -m venv .venv
     - .\.venv\Scripts\Activate.ps1
   - CMD example:
     - python -m venv .venv
     - .\.venv\Scripts\activate.bat
2. Install dependencies:
   - pip install -r requirements.txt
3. Add environment variables (see `.env.example` below) or export them in terminal.
4. Run migrations:
   - python manage.py migrate
5. (Optional) Create superuser:
   - python manage.py createsuperuser
6. Run dev server:
   - python manage.py runserver 127.0.0.1:8000

## Quickstart — Frontend

1. Open terminal in `frontend`:
   - npm install
   - npm start
2. Default dev UI served at http://localhost:3000

## Environment (.env) — example keys

- SECRET_KEY=<replace_with_secure_value>
- DEBUG=True
- ALLOWED_HOSTS=127.0.0.1,localhost
- DATABASE_URL=sqlite:///db.sqlite3 (or PostgreSQL URL)
- CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

Note: Update Django settings to read SECRET_KEY and DEBUG from env in production.

## Database & Models (summary)

- User (custom user model `api.User`)
  - fields: email/username, name, role (student|staff|admin), is_active
- Equipment
  - fields: id, name, category, condition, total_quantity, available_quantity, metadata
- BorrowRequest
  - fields: id, requester (User), equipment (FK), quantity, start_date, end_date, status (pending|approved|rejected|issued|returned), issued_by (User), returned_at, notes
- Audit/History (optional): logs of issues/returns

## API Endpoints (examples)

Base: http://127.0.0.1:8000/api/

Authentication

- POST /api/auth/signup/ — create account
- POST /api/auth/login/ — returns access and refresh tokens (JWT)
- POST /api/auth/token/refresh/ — refresh token

Equipment

- GET /api/equipment/ — list (supports query params: ?category=&available=true)
- POST /api/equipment/ — create (admin)
- GET /api/equipment/{id}/ — retrieve
- PUT /api/equipment/{id}/ — update (admin)
- DELETE /api/equipment/{id}/ — delete (admin)

Requests / Borrowing

- POST /api/requests/ — create borrow request (student/staff)
- GET /api/requests/ — list (admins see all; users see own)
- GET /api/requests/{id}/
- POST /api/requests/{id}/approve/ — approve (staff/admin)
- POST /api/requests/{id}/reject/ — reject
- POST /api/requests/{id}/issue/ — mark issued (decrement inventory)
- POST /api/requests/{id}/return/ — mark returned (increment inventory)

Search & Filters

- GET /api/equipment/?q=term
- GET /api/equipment/?category=Camera&available=true

Example curl (login):
curl -X POST http://127.0.0.1:8000/api/auth/login/ -H "Content-Type: application/json" -d "{\"username\":\"user\",\"password\":\"pass\"}"

Authorization: Include header "Authorization: Bearer <access_token>" for protected endpoints.

## Preventing Overlaps

- Backend validates requested date ranges and quantities against approved/issued requests.
- New requests fail with 409 or validation error when overlap detected.

## Roles & Permissions

- Student: request equipment, view own requests
- Staff: approve/issue/return requests, view equipment
- Admin: full CRUD on equipment, manage users, view analytics

## Tests

- Backend:
  - python manage.py test api
- Frontend:
  - npm test

## Deployment (brief)

- Use production-ready secrets (SECRET_KEY), DEBUG=False, proper ALLOWED_HOSTS.
- Use PostgreSQL or other production DB.
- Serve static files (collectstatic) and configure CORS and CSRF origins for frontend host.
- Consider Docker + docker-compose (compose file included).

## Contributing

- Fork -> feature branch -> PR with tests -> review -> merge.
- Follow code style for Python (black/flake8) and JS/TS (prettier/eslint).

## Troubleshooting

- "Allowed hosts" errors: set ALLOWED_HOSTS env or adjust settings.
- CORS issues: ensure frontend origin is in CORS_ALLOWED_ORIGINS.
- DB errors: confirm migrations applied and DB path URI correct.

## Notes

- Current development settings may contain example SECRET_KEY in repository; rotate before production.
- Extend with notifications, scheduling calendar, inventory reports, and file attachments as needed.

License

- Add your preferred license file (e.g., MIT) to this repo.
