#coding utf-8

import socket

porta = 1717
host = '127.0.0.1'

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', porta))
serverSocket.listen(1)

connectionSocket, addr = serverSocket.accept()
connectionSocket.settimeout(60)

while True:
    request = connectionSocket.recv(1024).decode()

    print(request)


