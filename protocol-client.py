#!/usr/bin/env python3

import socket

HOST = socket.gethostname()
PORT = 60001

SOCKET = socket.socket()

try:
    SOCKET.connect((HOST, PORT))
    msg = ""

    while True:
        msg = input("Your Message: ")
        msg = msg.strip()
        SOCKET.send(msg.encode("utf-8"))

        if msg == "STOP":
            break
            

        """while True:
            data = SOCKET.recv(16)
            print(data)
            if data:
                recv_msg += data.decode("utf-8")
            else:
                break"""

        data = SOCKET.recv(1024)
        print(data.decode("utf-8"))

    SOCKET.close()
finally:
    SOCKET.close()
