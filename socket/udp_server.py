from socket import *

udp_server = socket(AF_INET, SOCK_DGRAM)
IP_port=("localhost", 8080)
udp_server.bind(IP_port)

while True:
    data, addr=udp_server.recvfrom(1024)
    print(data)
    print("server recieved", addr)
    udp_server.sendto(data.upper(), addr)

