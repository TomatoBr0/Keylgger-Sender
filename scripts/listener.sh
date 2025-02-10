#!/bin/bash

# Start Netcat listener to receive logs
nc -lvnp 5555 > received_logs.txt