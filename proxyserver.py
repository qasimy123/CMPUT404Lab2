#!/usr/bin/env python3
import os
import socket
import sys
import time

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
            print("Connected by", addr)

            # recieve data, wait a bit, then send it back
            full_data = conn.recv(BUFFER_SIZE)
            time.sleep(0.5)
            googles_response = get_google_response(full_data)
            conn.sendall(googles_response)
            conn.close()
            
        # Rewrite the code above to fork a process every time a connection is received.
        
        # while True:
        #     pid = os.fork()
        #     conn, addr = s.accept()
        #     print("Connected by", addr)
        #     # recieve data, wait a bit, then send it back
        #     full_data = conn.recv(BUFFER_SIZE)
        #     time.sleep(0.5)
        #     googles_response = get_google_response(full_data)
        #     conn.sendall(googles_response)
        #     conn.close()
        #     if pid == 0:
        #         exit(0)
        #     else:
        #         os.waitpid(pid, 0)


def get_google_response(payload):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('www.google.com', 80))
        s.sendall(payload)
        s.shutdown(socket.SHUT_WR)
        data = s.recv(BUFFER_SIZE)
        return data


if __name__ == "__main__":
    main()
