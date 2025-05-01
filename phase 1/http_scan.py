import requests
target ="http://192.168.56.109"
try:
    response = requests.get(target)
    print(f"[+] HTTP Response Code: {response.status_code}")
    print(f"[+] Server Header: {response.headers.get('Server')}")
    print(f"[+] X-Frame-Options header: {response.headers.get('X-Content-Type-Options')}")
    print(f"[+] X-Content-type-Options Header: {response.headers.get('X-Content-Type-Options')}")
except requests.exceptions.RequestException as e:
    print(f"[-] Error connecting to target: {e}")
