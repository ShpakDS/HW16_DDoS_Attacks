# HW16_DDoS_Attacks
HW16_DDoS_Attacks

## Setup
1. Run command `docker-compose up --build`
2. Go to container attacker  `docker exec -it attacker /bin/bash`
3. And use one of the following types of attacks 
```
   python3 /scripts/udp_flood.py
   python3 /scripts/http_flood.py
   python3 /scripts/syn_flood.py
   python3 /scripts/icmp_flood.py
```

Check logs defender:
Run command `docker logs defender`

To make sure the site is available, run the command `curl http://localhost:8080` and see result:

```<h1>Welcome to Defender</h1>```