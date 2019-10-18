#! /usr/bin/env python3

import socket

HOST = socket.gethostname()
PORT = 60001

SOCKET = socket.socket()

try:
    SOCKET.bind((HOST, PORT))
    SOCKET.listen()

    while True:
        conn, addr = SOCKET.accept()
        print(f"Client {addr[0]} connected at port {addr[1]}.")
        while True:
            #print("Running...")
            msg = conn.recv(1024)
            msg = msg.decode("utf-8")
            upper_msg = msg.upper()
            if msg and msg == "STOP":
                break
            else:
                conn.send(upper_msg.encode("utf-8"))
        conn.close()
        print("Client disconnected. Waiting for new client")
finally:
    SOCKET.close()
