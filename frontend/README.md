# Equipment Lending System - Frontend

React frontend for the Equipment Lending System built with Vite.

## Setup Instructions

### Prerequisites
- Node.js 16 or higher
- npm or yarn

### Installation

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

4. Update the `.env` file with your backend API URL (default is `http://localhost:8000/api`)

5. Start the development server:
```bash
npm run dev
```

The application will be available at `http://localhost:5173`

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## Project Structure

```
frontend/
├── public/              # Static assets
├── src/
│   ├── components/      # Reusable components
│   │   └── Header.jsx
│   ├── pages/           # Page components
│   │   ├── Home.jsx
│   │   ├── EquipmentList.jsx
│   │   └── LendingRecords.jsx
│   ├── services/        # API service layer
│   │   └── api.js
│   ├── App.jsx          # Main app component
│   ├── App.css          # App styles
│   ├── main.jsx         # Entry point
│   └── index.css        # Global styles
├── .env.example         # Environment variables template
├── package.json         # Dependencies
└── vite.config.js       # Vite configuration
```

## Features

### Home Page
- Welcome page with system overview
- Feature highlights
- Getting started guide

### Equipment List
- View all available equipment
- Display equipment details (name, category, description)
- Show availability status and quantities

### Lending Records
- View all lending transactions
- Filter by status
- Display record details (dates, user, status)

## Technologies Used

- **React** - UI library
- **Vite** - Build tool
- **React Router** - Routing
- **Axios** - HTTP client
- **CSS** - Styling

## Connecting to Backend

The frontend connects to the Django backend API. Make sure:
1. The backend server is running on `http://localhost:8000`
2. CORS is properly configured in the backend
3. The API URL in `.env` matches your backend URL

## Extending the Application

This boilerplate provides a foundation to add features like:
- User authentication
- Equipment booking/reservation
- Admin dashboard
- File uploads
- Real-time notifications
- Advanced filtering and search
- User profiles
- Equipment history tracking
