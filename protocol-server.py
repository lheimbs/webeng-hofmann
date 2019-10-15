#! /usr/bin/env python

import socket

HOST = socket.gethostname()
PORT = 60000

SOCKET = socket.socket()

try:
    SOCKET.bind((HOST, PORT))
    SOCKET.listen()

    while True:
        conn, addr = SOCKET.accept()
        msg = conn.recv(1024)
        upper_msg = msg.decode("utf-8").upper()
        print(upper_msg)
        conn.send(upper_msg.encode("utf-8"))
        conn.close()
finally:
    SOCKET.close()
