#!/usr/bin/env python3
import socket
import time
import multiprocessing

'''
Credit: Code from CMPUT404 Lab Instructors 
'''

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            multiprocessing.Process(target=handle_request, args=(conn, addr)).start()
            conn.close()

def handle_request(conn, addr):
    print("Connected by", addr)
            
            #recieve data, wait a bit, then send it back
    full_data = conn.recv(BUFFER_SIZE)
    time.sleep(0.5)
    print(full_data)
    conn.sendall(full_data)
    

if __name__ == "__main__":
    main()
