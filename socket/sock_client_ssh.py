import socket
import struct
from functools import partial
client = socket.socket()

client.connect(('localhost', 9999))

while True:
    cmd = input('>>:').strip()
    if len(cmd) == 'quit': break

    client.send(cmd.encode('utf-8'))
    length_tuple = client.recv(4)
    cmd_res_size = struct.unpack('i',length_tuple)[0]  # 4 bytes due to struct, with not stick with after recv

    if cmd_res_size:
        print("size:", cmd_res_size)
        # # send data server in case of stopping
        # client.send("it is ready to get data".encode("utf-8")) # won't need  send data any more, method 2
        # will not stick with after recv
    recv_data=""
    recv_size=0
    while recv_size < int(cmd_res_size):
        recv_data += client.recv(1000000).decode()
        recv_size = len(recv_data)
    else:
        print("cmd res received...", recv_size)
        print(recv_data)
    # fin_msg = iter(partial(client.recv, 1024), b'')  #iter get the return data compare with b''
    # print(fin_msg)
client.close()
