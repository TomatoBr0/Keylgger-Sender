CC = gcc
CFLAGS = -framework ApplicationServices

all: keylogger

keylogger: keylogger.c
	$(CC) $(CFLAGS) -o keylogger keylogger.c

clean:
	rm -f keylogger