
```
import wifi
import socketpool

# Replace with your WiFi credentials
ssid = "YOUR_WIFI_SSID"
password = "YOUR_WIFI_PASSWORD"

print("Connecting to WiFi...")
wifi.radio.connect(ssid, password)
print("Connected, IP address:", wifi.radio.ipv4_address)

# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)

# Create UDP socket
sock = pool.socket(pool.AF_INET, pool.SOCK_DGRAM)

# Bind to port 3615 on your device's IP
sock.bind((str(wifi.radio.ipv4_address), 3615))
print("Listening on UDP port 3615...")

# Buffer for incoming data
buffer = bytearray(1024)

while True:
    try:
        nbytes, addr = sock.recvfrom_into(buffer)
        if nbytes:
            data = buffer[:nbytes]
            print("Received from", addr, ":", data)
    except Exception as e:
        print("Error:", e)

```

```
import socket
import time

# Target IP: replace with your CircuitPython board's IP  http://192.168.178.67:5000
TARGET_IP = "192.168.178.67"   # Example, change to your board's IP
TARGET_PORT = 3615

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Sending UDP packets to {TARGET_IP}:{TARGET_PORT}...")

counter = 0
while True:
    message = f"Packet #{counter}".encode("utf-8")
    sock.sendto(message, (TARGET_IP, TARGET_PORT))
    print(f"Sent: {message}")
    counter += 1
    time.sleep(1)  # send one packet per second

```
