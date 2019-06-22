import socket
import struct
import os
import time
import subprocess
server = socket.socket()
server.bind(('localhost', 9999))
server.listen()

while True:
    conn, addr = server.accept()
    print(addr)
    print("new conn", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("client has disconnected")
            break
        print("exec cmd:", data)
        # cmd_res = os.popen(data.decode()).read()
        # exce command and get err or output from pipe
        res = subprocess.Popen(data.decode('utf-8'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
        err = res.stderr.read()
        if err:
            cmd_res = err
        else:
            cmd_res = res.stdout.read()
        print("before send", len(cmd_res))
        if not cmd_res:
            cmd_res = "cmd execute successfully".encode('utf-8')
        encode_cmd_res = cmd_res
        # conn.send(str(len(cmd_res)).encode('utf-8')) # method 2 send length between 2 receive
        # client_ack = conn.recv(1024) # wait client to confirm method 2 waiting for receive msg from client after above
        # new solution, do not need receive the data back as method 2
        size = struct.pack('i', len(cmd_res))  # transfer cmd_res to 4 bytes
        conn.send(size)
        # time.sleep(0.5) # stop two result sent stick together method 1

        conn.send(encode_cmd_res)
        print('send done')


server.close()