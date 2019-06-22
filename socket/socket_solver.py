import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('conn is ', self.request)  #conn
        print('addr is ',self.client_address)
        while True:
            try:
                # getting msg
                data = self.request.recv(1024)
                print('message from client: ', data)
                # send msg
                self.request.sendall(data.upper())
            except Exception as e:
                print(e)
                break


if __name__== '__main__':

    s = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), MyServer) # same as the inter loop, 线程
    # s = socketserver.ForkingTCPServer(('127.0.0.1', 8080), MyServer) # same as the inter loop 进程 cost more

    s.serve_forever()  #  keep conn status like while True: conn, addr = server.accept()