#!/usr/bin/env python3
import os
import socket
import sys
import time
import multiprocessing

# define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 4096


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # bind socket to address
        s.bind((HOST, PORT))
        # set to listening mode
        s.listen(2)

        # # continuously listen for connections
        while True:
            conn, addr = s.accept()
            multiprocessing.Process(
                target=handle_request, args=(conn, addr)).start()
            conn.close()


def handle_request(conn, addr):
    full_data = b""
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        full_data += data
    print(full_data.decode())
    time.sleep(0.5)
    googles_response = get_google_response(full_data)
    conn.sendall(googles_response)


def get_google_response(payload):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        GOOGLE_IP = socket.gethostbyname("www.google.com")
        s.connect((GOOGLE_IP, 80))
        s.sendall(payload)
        s.shutdown(socket.SHUT_WR)
        full_data = b""
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            full_data += data
        return full_data


if __name__ == "__main__":
    main()
