# Conquest

A digital board game implementation with cross-platform support.

## Monorepo Structure

This repository is organized as a monorepo containing three main applications:

```
conquest/
├── backend/          # Django REST API with MongoDB
├── frontend/         # React web application
├── mobile/           # React Native (Expo) mobile app
└── resources/        # Shared assets and documentation
```

## Quick Start

### Prerequisites

- **Backend**: Python 3.8+, MongoDB
- **Frontend**: Node.js 16+, npm/yarn
- **Mobile**: Node.js 16+, Expo CLI

### Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/GreedosBurritos/Conquest.git
   cd Conquest
   ```

2. **Backend Setup** (Django + MongoDB):
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env      # Configure your environment
   python manage.py migrate
   python manage.py runserver
   ```

3. **Frontend Setup** (React):
   ```bash
   cd frontend
   npm install
   cp .env.example .env.local  # Configure your environment
   npm run dev
   ```

4. **Mobile Setup** (React Native + Expo):
   ```bash
   cd mobile
   npm install
   cp .env.example .env        # Configure your environment
   npm start
   ```

## Architecture Overview

- **Backend**: Django REST API serves game logic, user management, and data persistence
- **Frontend**: React web app for desktop/browser gameplay
- **Mobile**: React Native app for iOS/Android with touch-optimized interface
- **Database**: MongoDB for flexible game state and user data storage

## Development Workflow

1. Start the backend API server first
2. Run frontend and/or mobile apps
3. All applications communicate with the same backend API
4. Real-time features (future) will use WebSocket connections

## Project Status

🚧 **Currently in development** - This is the initial scaffolding phase.

### Completed
- [x] Monorepo structure setup
- [x] Backend scaffolding (Django + MongoDB)
- [x] Frontend scaffolding (React + Vite)
- [x] Mobile scaffolding (React Native + Expo)

### Planned Features
- [ ] User authentication and authorization
- [ ] Game logic implementation
- [ ] Real-time multiplayer functionality
- [ ] Game state persistence
- [ ] Mobile-optimized UI/UX
- [ ] Deployment configurations

## Contributing

Each subdirectory contains its own README with specific setup instructions and development guidelines. Please refer to the individual README files for detailed information about each application.

## License

[Add your license information here]

# Conquest Project Reset

This repository has been reset to a clean state as of June 2025. All previous code, configuration, and project files have been removed to allow for a fresh start.

## Next Steps
- Re-initialize backend, frontend, and mobile apps as needed.
- Set up new project structure and dependencies.
- See project issues for further instructions or planning.
