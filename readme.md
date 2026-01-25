# SpendSense-backend

## Running the Development Server

To avoid ModuleNotFoundError issues with the src/ layout, use the provided script or set the PYTHONPATH manually:

### Option 1: Use the provided script (Windows PowerShell)

    ./run_dev.ps1

This sets the PYTHONPATH to src and starts the FastAPI dev server.

### Option 2: Set PYTHONPATH manually (Windows PowerShell)

    $env:PYTHONPATH = "src"
    fastapi dev src/main.py

### Option 3: Run from project root using module path

    fastapi dev src.main

> **Note:** Always run these commands from the project root (where the src folder is located).

---

## Project Structure

    src/
      api/
      db/
      models/
      service/
      utils/
      main.py
      config.py
    requirements.txt
    Dockerfile
    run_dev.ps1
    README.md

---

## Logging

Logs are written to both the console and to logs/app.log. The logs directory is created automatically if it does not exist.
