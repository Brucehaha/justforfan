import socketserver


class UdpmyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('Get the msg from client', self.request[0])
        print('Client', self.client_address)
        print('Client', self.request[1])

        self.request[1].sendto(self.request[0].upper(), self.client_address)


if __name__ == '__main__':
    s = socketserver.ThreadingUDPServer(('127.0.0.1', 8081), UdpmyServer) # same as the inter loop, 线程
    # s = socketserver.ForkingTCPServer(('127.0.0.1', 8080), MyServer) # same as the inter loop 进程 cost more

    s.serve_forever()  #   keep conn status like while True: conn, addr = server.accept()