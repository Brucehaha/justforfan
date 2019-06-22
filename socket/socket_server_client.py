import socket
import struct
from functools import partial
client = socket.socket()

client.connect(('localhost', 8081))

while True:
    cmd = input('>>:').strip()
    if len(cmd) == 'quit': break
    client.sendall(cmd.encode('utf-8'))
    recv_data = client.recv(1000000).decode()
    print(recv_data)

client.close()
