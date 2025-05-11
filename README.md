# Disease Outbreak Prediction System

A web application for predicting disease outbreaks using machine learning models.

## Features

- User authentication with Firebase
- Two-factor authentication (2FA) for enhanced security
- Interactive dashboard for disease outbreak prediction
- Risk analysis and visualization
- Historical trend analysis

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Firebase project with Authentication enabled

### Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd disease-outbreak-prediction-main
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Configure Firebase:
   - Create a Firebase project at [Firebase Console](https://console.firebase.google.com/)
   - Enable Email/Password authentication method
   - Download your Firebase service account key and save it as `firebase-key.json` in the project root directory

4. Set environment variables:
   ```
   # Linux/macOS
   export SECRET_KEY="your-secret-key"

   # Windows
   set SECRET_KEY=your-secret-key
   ```

## Running the Application

### Using the provided scripts

#### On Linux/macOS:
```
chmod +x setup_and_run.sh
./setup_and_run.sh
```

#### On Windows:
```
powershell -ExecutionPolicy Bypass -File setup_and_run.ps1
```

### Manual execution
```
python src/app.py
```

The application will be available at `http://localhost:8050`

## Usage

1. Register a new account
2. Set up two-factor authentication (optional but recommended)
3. Use the dashboard to input parameters and analyze outbreak risks
4. View predictions and recommendations based on the input data

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'pyotp'**
   - Make sure you've installed all required packages: `pip install -r requirements.txt`

## License

This project is licensed under the MIT License - see the LICENSE file for details. 