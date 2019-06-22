import selectors
import os
import socket
import json
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class MyFtpServer:
    def __init__(self):
        self.last = 0
        self.sel = selectors.DefaultSelector()
        self.conns = {}
        self.make_connect()
        self.handle()

    def make_connect(self):
        server = socket.socket()
        server.bind(('localhost',8080))
        server.listen(5)
        self.sel.register(server, selectors.EVENT_READ, self.accept)
        print('server has started ')

    def handle(self):
        while True:
            events = self.sel.select()  # sock server, conn
            for key, mask in events:
                callback = key.data
                callback(key.fileobj, mask)

    def accept(self, sock, mask):
        conn, addr = sock.accept()  # Should be ready
        print('accepted', conn, 'from', addr)
        conn.setblocking(False)
        self.sel.register(conn, selectors.EVENT_READ, self.read)
        self.conns[conn] = {}

    def read(self, conn, mask):

        try:
            if self.conns[conn]:
                func = getattr(self, self.conns[conn]['action'])
                func(conn)
            else:
                data = conn.recv(1024)
                data = json.loads(data.decode('utf8'))
                if hasattr(self, data['action']):
                    self.conns[conn]['action'] = data['action']
                    self.conns[conn]['file_size'] = data['file_size']
                    self.conns[conn]['file_name'] = data['file_name']
                    self.conns[conn]['has_size'] = 0
                    conn.send(b'800')
                    func = getattr(self, data['action'])
                    func(conn)
        except Exception as e:
            print('error', e)
            # self.sel.unregister(conn)
            # conn.close

    def upload(self, conn):
        file_size = self.conns[conn]['file_size']
        file_name = self.conns[conn]['file_name']
        file_path = os.path.join(BASE_DIR, 'upload', file_name)
        data = conn.recv(1024)
        self.conns[conn]['has_size'] += len(data)
        with open(file_path, 'ab') as f:
            f.write(data)
        if self.conns[conn]['has_size'] == file_size:
            if conn in self.conns.keys():
                self.conns[conn] = {}
            print(" File has been uploaded")

    def download(self, conn):
        pass


if __name__ == '__main__':

    MyFtpServer()



