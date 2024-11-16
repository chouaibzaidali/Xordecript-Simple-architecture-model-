@echo off

REM Check if virtual environment is activated
if "%VIRTUAL_ENV%"=="" (
    echo Please activate your virtual environment before running this script.
    exit /b 1
)

REM Install dependencies from requirements.txt
pip install -r requirements.txt

echo All dependencies have been installed successfully!