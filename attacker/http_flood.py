import requests

url = "http://defender:8080"

while True:
    try:
        requests.get(url)
    except:
        pass