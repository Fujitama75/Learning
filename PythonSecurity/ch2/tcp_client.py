#!/usr/bin/python

import socket

# (プロトコルファミリ、ソケットタイプ)
# TCP: (IPv4プロトコルファミリ、ストリーム通信)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 50000

server = (ip, port)
sock.connect(server)

msg = ''
while msg != 'exit':
    msg = input('-> ')

    sock.send(msg.encode())

    data = sock.recv(1024)

    print('Receivec from server: ', str(data))

sock.close()