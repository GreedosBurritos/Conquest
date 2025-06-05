# Conquest Mobile

React Native mobile app with Expo for the Conquest board game.

## Tech Stack

- **Framework**: React Native with Expo
- **Navigation**: React Navigation
- **State Management**: React Context / Redux Toolkit
- **HTTP Client**: Axios
- **UI Components**: React Native Elements / NativeBase
- **Platform**: iOS and Android

## Setup Instructions

### Prerequisites

- Node.js 16+
- npm or yarn
- Expo CLI (`npm install -g @expo/cli`)
- Expo Go app on your mobile device (for testing)

### Installation

1. Navigate to the mobile directory:
   ```bash
   cd mobile
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API endpoint and other settings
   ```

4. Start the Expo development server:
   ```bash
   npm start
   # or
   yarn start
   ```

5. Use Expo Go app to scan the QR code and run on your device, or run in simulators:
   ```bash
   npm run ios      # iOS Simulator
   npm run android  # Android Emulator
   ```

## Project Structure

```
mobile/
├── assets/           # Images, fonts, and other static assets
├── src/
│   ├── components/   # Reusable React Native components
│   ├── screens/      # Screen components
│   ├── navigation/   # Navigation configuration
│   ├── hooks/        # Custom React hooks
│   ├── services/     # API service functions
│   ├── store/        # State management
│   ├── styles/       # Styling and theme configuration
│   ├── utils/        # Utility functions
│   └── App.js        # Main App component
├── app.json          # Expo configuration
├── package.json      # Dependencies and scripts
├── babel.config.js   # Babel configuration
└── .env.example      # Environment variables template
```

## Available Scripts

- `npm start` - Start Expo development server
- `npm run ios` - Run on iOS simulator
- `npm run android` - Run on Android emulator
- `npm run web` - Run in web browser (Expo web)
- `npm run lint` - Run ESLint
- `npm test` - Run tests

## Environment Variables

Create a `.env` file with the following variables:

```
API_BASE_URL=http://localhost:8000/api
APP_VARIANT=development
```

## Development Notes

- Uses Expo managed workflow for easier development and deployment
- Game board will be optimized for touch interactions
- Supports both portrait and landscape orientations
- Push notifications can be added later for game updates
- Expo EAS Build for production app builds

## Building for Production

1. Install EAS CLI:
   ```bash
   npm install -g eas-cli
   ```

2. Configure EAS:
   ```bash
   eas build:configure
   ```

3. Build for app stores:
   ```bash
   eas build --platform all
   ```