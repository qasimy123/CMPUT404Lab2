#!/usr/bin/env python3
import socket
import sys

# create a tcp socket


def create_tcp_socket():
    print('Creating socket')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error):
        print(
            f'Failed to create socket. Error code:')
        sys.exit()
    print('Socket created successfully')
    return s

# get host information


def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    print(f'Ip address of {host} is {remote_ip}')
    return remote_ip

# send data to server


def send_data(serversocket, payload):
    print("Sending payload")
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print('Send failed')
        sys.exit()
    print("Payload sent successfully")


def main():
    try:
        # define address info, payload, and buffer size
        host = '127.0.0.1'
        port = 8001
        payload = f'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'
        buffer_size = 4096

        # make the socket, get the ip, and connect
        s = create_tcp_socket()
        # connect to local host
        s.connect((host, port))
        print(f'Socket Connected to {host}')

        # send the data and shutdown
        send_data(s, payload)
        s.shutdown(socket.SHUT_WR)

        # continue accepting data until no more left
        full_data = b""
        while True:
            data = s.recv(buffer_size)
            if not data:
                break
            full_data += data
        print("Client", full_data)
    except Exception as e:
        print(e)
    finally:
        # always close at the end!
        s.close()


if __name__ == "__main__":
    main()
