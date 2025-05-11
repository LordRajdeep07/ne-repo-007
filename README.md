# Disease Outbreak Prediction System

A comprehensive web application for predicting disease outbreaks using machine learning models based on climate and health data.

## Features

- User authentication with Firebase
- Two-factor authentication (2FA) for enhanced security
- Interactive dashboard for disease outbreak prediction
- Risk analysis and visualization
- Historical trend analysis
- Data generation tools for testing and development

## Repository Structure

- `src/` - Main application code
- `data/` - Data files for the application
  - `raw/climate/` - Climate data
  - `raw/health/` - Health data
  - `processed/` - Merged and processed data
- `models/` - Machine learning models
- `templates/` - HTML templates for the web interface
- `static/` - Static assets (CSS, JS, images)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Firebase project with Authentication enabled (optional for full functionality)

### Setup Options

#### Option 1: One-click installation (Windows)

1. Run `Install_Requirements.bat` by double-clicking it
2. Follow the on-screen instructions

#### Option 2: Using setup scripts

**On Windows:**
```
powershell -ExecutionPolicy Bypass -File setup_and_run.ps1
```

**On Linux/macOS:**
```
chmod +x setup_and_run.sh
./setup_and_run.sh
```

#### Option 3: Manual installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd disease-outbreak-prediction
   ```

2. Create and activate a virtual environment (recommended):
   ```
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python src/app.py
   ```

## Data Generation

The repository includes scripts for generating realistic disease outbreak data:

- `generate_data.py` - Generates initial dataset
- `generate_more_data.py` - Adds more data to the merged dataset
- `update_all_data_files.py` - Updates all data files (climate, health, and merged) consistently

To generate new data:
```
python update_all_data_files.py
```

## Usage

1. Start the application using one of the setup methods above
2. Register a new account (if authentication is enabled)
3. Use the dashboard to input parameters and analyze outbreak risks
4. View predictions and recommendations based on the input data

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**
   - Make sure you've installed all required packages: `pip install -r requirements.txt`
   - Ensure you're running the application from the correct directory

2. **Data file errors**
   - If data files are missing, run `python update_all_data_files.py` to generate them

3. **Authentication issues**
   - For local testing without Firebase, you can bypass authentication by modifying `src/app.py`

## License

This project is licensed under the MIT License - see the LICENSE file for details. 