#!/usr/bin/env python
"""
Environment checker for Disease Outbreak Prediction System
This script verifies that all necessary dependencies and data files are present.
"""

import os
import sys
import importlib
import subprocess
import platform

def print_header(message):
    """Print a formatted header message."""
    print("\n" + "="*80)
    print(f" {message}")
    print("="*80)

def check_python_version():
    """Check if Python version is compatible."""
    print_header("Checking Python version")
    
    major, minor = sys.version_info[:2]
    print(f"Python version: {major}.{minor}")
    
    if major < 3 or (major == 3 and minor < 8):
        print("❌ Python 3.8 or higher is required")
        return False
    else:
        print("✅ Python version is compatible")
        return True

def check_dependencies():
    """Check if all required packages are installed."""
    print_header("Checking dependencies")
    
    required_packages = [
        "pandas", "numpy", "matplotlib", "seaborn", "dash", "dash_bootstrap_components",
        "flask", "flask_login", "plotly", "joblib", "requests"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package} is installed")
        except ImportError:
            print(f"❌ {package} is not installed")
            missing_packages.append(package)
    
    if missing_packages:
        print("\nMissing packages:", ", ".join(missing_packages))
        install = input("\nWould you like to install missing packages? (y/n): ")
        if install.lower() == 'y':
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            return check_dependencies()  # Recheck after installation
        return False
    
    return True

def check_data_files():
    """Check if necessary data files exist."""
    print_header("Checking data files")
    
    data_paths = [
        "data/raw/climate/mock_climate_data.csv",
        "data/raw/health/mock_outbreak_data.csv",
        "data/processed/merged_data.csv"
    ]
    
    missing_files = []
    
    for path in data_paths:
        if os.path.exists(path):
            print(f"✅ {path} exists")
        else:
            print(f"❌ {path} is missing")
            missing_files.append(path)
    
    if missing_files:
        print("\nSome data files are missing.")
        generate = input("\nWould you like to generate the missing data files? (y/n): ")
        if generate.lower() == 'y':
            try:
                print("\nGenerating data files...")
                subprocess.check_call([sys.executable, "update_all_data_files.py"])
                return check_data_files()  # Recheck after generation
            except Exception as e:
                print(f"Error generating data files: {e}")
                return False
        return False
    
    return True

def check_models():
    """Check if model files exist."""
    print_header("Checking model files")
    
    model_dir = "models"
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
        print(f"✅ Created {model_dir} directory")
    else:
        print(f"✅ {model_dir} directory exists")
    
    # Check for specific model files if needed
    model_path = os.path.join("src", "models", "outbreak_model.pkl")
    if os.path.exists(model_path):
        print(f"✅ ML model exists at {model_path}")
    else:
        print(f"⚠️ ML model not found at {model_path} (will be created when needed)")
    
    return True

def check_directories():
    """Check if necessary directories exist and create them if needed."""
    print_header("Checking directories")
    
    directories = [
        "data",
        "data/raw",
        "data/raw/climate",
        "data/raw/health",
        "data/processed",
        "models",
        "src/models"
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✅ Created {directory} directory")
        else:
            print(f"✅ {directory} directory exists")
    
    return True

def main():
    """Main function to run all checks."""
    print_header("Disease Outbreak Prediction System - Environment Check")
    
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Working Directory: {os.getcwd()}")
    
    checks = [
        check_python_version,
        check_directories,
        check_dependencies,
        check_data_files,
        check_models
    ]
    
    all_passed = True
    for check in checks:
        if not check():
            all_passed = False
    
    if all_passed:
        print_header("All checks passed! The environment is ready.")
        print("\nYou can now run the application with:")
        print("  python src/app.py")
    else:
        print_header("Some checks failed. Please resolve the issues before running the application.")
    
    return all_passed

if __name__ == "__main__":
    main() 