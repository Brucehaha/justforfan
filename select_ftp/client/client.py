import socket
import os
import json
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class clientHandler:
    def __init__(self):
        self.conn = socket.socket()
        self.mk_connection()
        self.last = 0

    def mk_connection(self):
        self.conn.connect(('localhost', 8080))

    def run(self):
        while 1:
            cmd = input(">> ").strip()
            cmd_list = cmd.split(' ')
            if hasattr(self, cmd_list[0]):
                func = getattr(self, cmd_list[0])
                func(*cmd_list)

    def upload(self, *args):
        file_name = args[1]
        file_path = os.path.join(BASE_DIR, file_name)
        file_size = os.stat(file_path).st_size
        data = {
            "action": 'upload',
            'file_name': file_name,
            'file_size': file_size,
        }
        self.conn.send(json.dumps(data).encode('utf8'))
        response = self.conn.recv(1024)
        has_sent = 0
        if response == b'800':
            with open(file_path, 'rb') as f:
                while has_sent < file_size:
                    words = f.read(1024)
                    self.conn.sendall(words)
                    has_sent += len(words)
                    self.progress_percent(has_sent, file_size)

    def download(self):
        pass

    def progress_percent(self, has, total):
        rate = float(has)/float(total)
        rate_num = int(rate*100)
        if self.last != rate_num:
            sys.stdout.write('\r{0}% {1}'.format(rate_num,'#'*rate_num))
        self.last = rate_num


if __name__ == '__main__':
    client = clientHandler()
    client.run()