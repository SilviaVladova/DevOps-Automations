import socket

ip = '35.214.179.201'
port = 22

s = socket.socket()
s.settimeout(2)

try:
    s.connect((ip, port))
    print(f"Port {port} is open")
except:
    print(f"Port {port} is closed or blocked")

s.close()
