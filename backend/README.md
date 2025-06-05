# Conquest Backend

Django backend with MongoDB integration for the Conquest board game.

## Tech Stack

- **Framework**: Django
- **Database**: MongoDB with Djongo/MongoEngine
- **API**: Django REST Framework
- **Authentication**: Django Authentication + JWT

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip
- MongoDB (local or cloud instance)

### Installation

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your MongoDB connection string and other settings
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/`

## Project Structure

```
backend/
├── conquest/           # Main Django project
├── apps/              # Django apps
│   ├── games/         # Game logic and models
│   ├── users/         # User management
│   └── api/           # API endpoints
├── requirements.txt   # Python dependencies
├── .env.example      # Environment variables template
└── manage.py         # Django management script
```

## Development

- API documentation will be available at `/api/docs/` (Swagger/OpenAPI)
- Admin interface at `/admin/`
- MongoDB collections will be automatically created based on Django models

## Environment Variables

Create a `.env` file with the following variables:

```
SECRET_KEY=your-secret-key
DEBUG=True
MONGODB_HOST=localhost
MONGODB_PORT=27017
MONGODB_NAME=conquest_db
```