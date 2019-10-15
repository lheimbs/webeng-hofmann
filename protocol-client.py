#!/usr/bin/env python

import socket

HOST = socket.gethostname()
PORT = 60000

SOCKET = socket.socket()

msg = input("Your Message: ")

SOCKET.connect((HOST, PORT))
SOCKET.send(msg.encode("utf-8"))

recv_msg = ""
while True:
    data = SOCKET.recv(16)
    if data:
        recv_msg += data.decode("utf-8")
    else:
        break
print(recv_msg)

SOCKET.close()
