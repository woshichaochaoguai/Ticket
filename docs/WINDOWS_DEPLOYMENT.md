# Deployment Guide: Windows Server 2012

This document explains how to set up the AI Support Assistant on a Windows Server 2012 machine. It includes instructions for installing dependencies, configuring the environment, and running both the back-end and front-end services.

## Prerequisites

1. **Windows Server 2012** (with administrator access)
2. **Internet connection** for installing software and fetching dependencies
3. **Google Gemini API key**
4. Optional: A tool such as **Git** for cloning the repository

## 1. Install Required Software

### 1.1 Install Python

1. Download Python 3.9+ from the [official website](https://www.python.org/downloads/windows/).
2. Run the installer and enable **"Add Python to PATH"**.
3. Open **Command Prompt** and verify:
   ```cmd
   python --version
   ```

### 1.2 Install Node.js

1. Download Node.js LTS (v16 or higher) from the [Node.js website](https://nodejs.org/).
2. Run the installer and keep the default options.
3. Verify:
   ```cmd
   node --version
   npm --version
   ```

### 1.3 Install Git (optional but recommended)

1. Download Git for Windows from [git-scm.com](https://git-scm.com/download/win).
2. Run the installer and allow Git to be used from the command line.
3. Verify:
   ```cmd
   git --version
   ```

## 2. Obtain the Project

Clone the repository or copy the project files onto the server. With Git installed, run:
```cmd
git clone <repository-url>
cd <repository-folder>
```
Otherwise, you can manually download and extract the project.

## 3. Configure the Back-end

1. Navigate into the `backend` folder:
   ```cmd
   cd backend
   ```
2. Create a file named `.env` and insert your Google Gemini API key:
   ```cmd
   echo GOOGLE_API_KEY="your_api_key_here" > .env
   ```
3. Install Python dependencies:
   ```cmd
   pip install -r requirements.txt
   ```

4. Verify that the repository is up to date and that the file `__init__.py`
   exists in the `backend` folder. This file marks the folder as a Python
   package so that imports work correctly when running `flask` directly from
   this directory.

## 4. Launch the Back-end Service

Run these commands from the `backend` directory:
```cmd
set FLASK_APP=app.py
set FLASK_ENV=development
flask run --port=5001
```
If successful, you should see a message similar to:
```
 * Running on http://127.0.0.1:5001
```
Leave this window open to keep the server running.

## 5. Configure and Launch the Front-end

Open a new Command Prompt window and navigate to the `frontend` folder:
```cmd
cd frontend
npm install
npm start
```
After a few moments, the React development server will open your browser at `http://localhost:3000`.

## 6. Using the Application

1. Place any knowledge-base documents (`.txt`, `.md`, `.docx`, `.xlsx`) in the `backend/knowledge_files` folder.
2. On the web interface (http://localhost:3000), paste a customer ticket in the input panel.
3. Click **AI智能处理** to generate the summary, troubleshooting analysis, and English reply draft.
4. Review the results and edit as needed.

## 7. Running as a Background Service (Optional)

For production deployments, you may want to run the services in the background using tools such as **NSSM** (the Non-Sucking Service Manager) or Windows Task Scheduler. The basic idea is to create a service that executes the back-end `flask run` command and another that runs `npm start` or a production build with `npm run build` served via IIS or another web server.

## 8. Troubleshooting

- Ensure that the `.env` file contains a valid API key.
- If ports 5001 or 3000 are blocked by a firewall, open them in Windows Firewall settings.
- Use `pip list` and `npm list` to verify installed packages.
- Check the console output for errors when starting either service.
- If you see `ImportError: attempted relative import with no known parent package`,
  confirm that `backend/__init__.py` exists and you have pulled the latest code.

With these steps, you should have a working instance of the AI Support Assistant on Windows Server 2012.