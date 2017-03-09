#!/usr/bin/python3

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind((socket.gethostname(), 1234))

mySocket.listen(5)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        URL = random.randint(0, 1000)
        print('HTTP request received:')
        print(recvSocket.recv(2048).decode('utf-8'))
        print ('Answering back...')
        status = 'HTTP/1.1 301 Moved Permanently'
        recvSocket.send(bytes(status + '\r\n' +
                        'Location: https://www.google.es/\r\n' +
                        '<html>'+
                        '<head>'+
                        '<title>Moved</title>'+
                        '</head>'+
                        '<body>'+
                        '<h1>Moved</h1>'+
                        '<p>This page has moved to <a href="http://www.google.es">http://www.google.es</a>.</p>'+
                        '</body>'+
                        '</html>'+
                        '\r\n\r\n', 'utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print ("Closing binded socket")
    mySocket.close()
