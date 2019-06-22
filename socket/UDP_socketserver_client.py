from socket import *


udp_client = socket(AF_INET, SOCK_DGRAM)
IP_port=("127.0.0.1", 8081)

while True:
    msg = input(">>: ").strip()
    udp_client.sendto(msg.encode('utf-8'), IP_port)
    data, addr=udp_client.recvfrom(1024)
    print(data)

