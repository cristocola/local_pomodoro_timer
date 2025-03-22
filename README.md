
# 🍅 Local Pomodoro Timer

  

A fully offline Pomodoro productivity tracker that runs entirely on your machine. No internet, no cloud—just local work with a beautiful UI, local logging via SQLite, and easy management via a system tray icon.

  

---

  

## Overview

  

This project provides a simple, visually appealing Pomodoro timer with the following features:

  

-  **Interactive Timer:** Adjust Pomodoro, break, and alarm durations.

-  **Animated UI:** Smooth animations, motivational quotes, and a modern design.

-  **Local Logging:** Completed pomodoros are recorded into a local SQLite database.

-  **Dual Interface:**

-  `index.html`: Main timer interface.

-  `index2.html`: Detailed log history showing daily pomodoro counts.

-  **Backend Services:**

- A static file server (port 8000) for serving the web files.

- A Flask API server (port 5000) for logging operations.

-  **System Tray Integration:** Control the app from the system tray.

-  **One-Click Launch:** A VBScript (`start_pomodoro.wsf`) that starts the server and opens your browser.

  

---

  

## Folder Structure

  

local_pomodoro_timer/

- alarm.mp3 # Alarm sound file

- favicon.ico # Web favicon

- gene_m34_icon.ico # Alternate icon (optional)

- icon.png # Tray icon image

- index.html # Main Pomodoro timer UI

- index2.html # Log history page

- Pomodoro Timer.lnk # Windows shortcut (if used)

- pomodoro_logs.db # SQLite database for logs

- pomodorsi.webp # Logo image for the UI

- server.py # Python backend (static server + Flask API + system tray)

- start_pomodoro.wsf # VBScript-based launcher

  

---

  

## How It Works

  

### Frontend

  

-  **index.html:**

The main user interface for the timer. Set your desired durations, start/pause the timer, and see motivational quotes. It uses JavaScript (via fetch calls) to communicate with the backend for logging completed pomodoros.

-  **index2.html:**

Displays a detailed log history with daily pomodoro counts.

  

### Backend (`server.py`)

  

-  **Static File Server (Port 8000):**

Uses a custom handler to securely serve your HTML, CSS, and media files, preventing directory listing.

-  **Flask API Server (Port 5000):**

Provides these endpoints:

-  `POST /log` – Save a new log entry.

-  `GET /logs` – Retrieve all log entries.

-  `POST /delete-last-log` – Delete the most recent log entry.

-  **System Tray Integration:**

Utilizes `pystray` and `Pillow` to display a tray icon, allowing you to exit the application gracefully.

  

### Launcher (`start_pomodoro.wsf`)

  

- Checks if the server is running.

- Starts `server.py` if needed.

- Opens your default web browser at `http://127.0.0.1:8000/index.html`.

  

---

  

## Installation

  

### Prerequisites

  

-  **Python 3.x** must be installed.

- Git is installed and configured.

  


## Steps to Set Up

### Clone the Repository (if you haven't already):

To get started, clone the repository and navigate into the project directory using the following commands:

bash

CollapseWrapCopy

`git clone https://github.com/cristocola/local_pomodoro_timer.git cd local_pomodoro_timer`

### (Optional) Create and Activate a Virtual Environment:

Setting up a virtual environment is recommended to isolate dependencies. Follow the instructions for your operating system:

#### For Windows:

bash

CollapseWrapCopy

`python -m venv venv venv\Scripts\activate`

#### For macOS/Linux:

bash

CollapseWrapCopy

`python -m venv venv source venv/bin/activate`

### Install Dependencies:

You need to install the required Python packages listed in a requirements.txt file.

1.  Create a file named requirements.txt with this content:
    
    ini
    
    CollapseWrapCopy
    
    `Flask==2.2.2  pystray==0.17.3  Pillow==9.4.0`
    
2.  Then, install the dependencies by running:
    
    bash
    
    CollapseWrapCopy
    
    `pip install -r requirements.txt`
    

### Start the Application:

You can launch the application in one of two ways:

-   **Option 1:** Double-click the file start_pomodoro.wsf.

OR

-   **Option 2:** Run it from the terminal with:
    
    bash
    
    CollapseWrapCopy
    
    `python server.py`
    

Then, open your browser and navigate to:  
[http://127.0.0.1:8000/index.html](http://127.0.0.1:8000/index.html)

  

---

  

## Usage

  

-  **Start a Pomodoro Session:**

Set your desired durations in the UI and click the appropriate buttons to start, pause, reset, or finish your pomodoro.

-  **View Logs:**

Click the "View Log History" link in the UI to open `index2.html` and see your daily progress.

-  **Exit the Application:**

Use the system tray icon to exit the application gracefully.

  

---

  

## Future Enhancements

  

- CSV export of logs.

- Graphical statistics of daily/weekly progress.

- Packaging as a desktop executable.

- Theme toggle (dark/light mode).

- Desktop notifications for session events.

  

---

  

## Privacy

  

- All data is stored locally in `pomodoro_logs.db`.

- The app runs entirely on `127.0.0.1` with no external data transmission.

  

---

  

## Author

  

**Cristo Cola**