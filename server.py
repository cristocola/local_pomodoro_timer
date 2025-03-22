# https server
from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading
import os

class SafeFileHandler(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        self.send_error(403, "Directory listing not allowed")
        return None

    def translate_path(self, path):
        # Restrict access to the script's directory only
        root_dir = os.path.dirname(os.path.abspath(__file__))
        requested_path = os.path.normpath(os.path.join(root_dir, path.lstrip('/')))
        if os.path.commonpath([root_dir, requested_path]) != root_dir:
            return os.path.join(root_dir, '404.html')  # Optional: create a 404.html fallback
        return requested_path

def run_static_server(port=8000):
    handler = SafeFileHandler
    handler.directory = os.path.dirname(os.path.abspath(__file__))  # Serve from script's folder
    httpd = HTTPServer(("127.0.0.1", port), handler)
    print(f"Serving files from: http://127.0.0.1:{port}")
    httpd.serve_forever()

# Start the server in the background
threading.Thread(target=run_static_server, daemon=True).start()

# === Your other code continues here ===
print("Main server running...")





#pomodoro log server

from flask import Flask, request, jsonify
import sqlite3
import os
import threading
import sys
from flask_cors import CORS
from pystray import Icon, MenuItem, Menu
from PIL import Image

app = Flask(__name__)
CORS(app)

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pomodoro_logs.db")

# Ensure database exists and has correct structure
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL
            )
        """)
        conn.commit()

init_db()

@app.route("/log", methods=["POST"])
def save_log():
    data = request.json
    log_entry = data.get("logEntry", "")
    
    if log_entry:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO logs (timestamp) VALUES (?)", (log_entry,))
            conn.commit()
        print(f"✅ Log saved: {log_entry}")
        return jsonify({"message": "Log saved successfully!"}), 200
    
    return jsonify({"error": "Invalid log entry"}), 400

@app.route("/logs", methods=["GET"])
def get_logs():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT timestamp FROM logs")
        logs = [row[0] for row in cursor.fetchall()]
    return jsonify({"logs": logs}), 200

@app.route("/delete-last-log", methods=["POST"])
def delete_last_log():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        # Get the id of the last logged entry
        cursor.execute("SELECT id FROM logs ORDER BY id DESC LIMIT 1")
        last_id = cursor.fetchone()[0]
        
        if last_id is not None:
            # Delete the last logged entry from the database
            cursor.execute("DELETE FROM logs WHERE id = ?", (last_id,))
            conn.commit()
            print(f"🚫 Deleted last log: {last_id}")
            return jsonify({"message": "Last log deleted successfully!"}), 200
        
        return jsonify({"error": "No logs found to delete"}), 400

# Function to start the Flask server in a separate thread
def start_flask_server():
    print("🚀 Flask server running at http://127.0.0.1:5000/")
    app.run(debug=False, port=5000, use_reloader=False)

# Function to exit the application from the system tray
def exit_program(icon, item):
    print("❌ Exiting server...")
    icon.stop()
    sys.exit()

# Load a small icon for the system tray (replace 'icon.png' with your image)
ICON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.png")

if not os.path.exists(ICON_PATH):
    # Create a placeholder icon if not provided
    img = Image.new("RGB", (64, 64), color=(255, 0, 0))  # Red square icon
    img.save(ICON_PATH)

image = Image.open(ICON_PATH)

# Create system tray menu
menu = Menu(MenuItem("Exit", exit_program))

# Create the system tray icon
icon = Icon("FlaskServer", image, "Flask Server Running", menu)

# Start the Flask server in a separate thread
server_thread = threading.Thread(target=start_flask_server, daemon=True)
server_thread.start()

# Run the system tray icon
icon.run()
