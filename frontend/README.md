# Conquest Frontend

React web frontend for the Conquest board game.

## Tech Stack

- **Framework**: React 18
- **Build Tool**: Vite
- **Styling**: CSS Modules / Styled Components
- **State Management**: React Context / Redux Toolkit
- **HTTP Client**: Axios
- **Routing**: React Router

## Setup Instructions

### Prerequisites

- Node.js 16+
- npm or yarn

### Installation

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env.local
   # Edit .env.local with your API endpoint and other settings
   ```

4. Start the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

The application will be available at `http://localhost:3000/`

## Project Structure

```
frontend/
├── public/            # Static assets
├── src/
│   ├── components/    # Reusable React components
│   ├── pages/         # Page components
│   ├── hooks/         # Custom React hooks
│   ├── services/      # API service functions
│   ├── store/         # State management
│   ├── styles/        # Global styles and themes
│   ├── utils/         # Utility functions
│   ├── App.jsx        # Main App component
│   └── main.jsx       # Entry point
├── package.json       # Dependencies and scripts
├── vite.config.js     # Vite configuration
└── .env.example       # Environment variables template
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build locally
- `npm run lint` - Run ESLint
- `npm test` - Run tests

## Environment Variables

Create a `.env.local` file with the following variables:

```
VITE_API_BASE_URL=http://localhost:8000/api
VITE_APP_TITLE=Conquest
```

## Development Notes

- The frontend communicates with the Django backend API
- Game board rendering will use HTML5 Canvas or SVG
- Real-time features (if implemented) will use WebSocket connections