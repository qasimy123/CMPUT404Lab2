# CMPUT404 Lab 2

## Question 1: How do you specify a TCP socket in Python?

In Python, you can specify a TCP socket by using the socket.socket() function. This function takes two parameters: the first is the address family, and the second is the socket type. The address family is AF_INET, and the socket type is SOCK_STREAM.

## Question 2: What is the difference between a client socket and a server socket in Python?

The difference between a client socket and a server socket in Python is that a client socket is used to connect to a server socket. A server socket is used to listen for incoming connections.

## Question 3: How do we instruct the OS to let us reuse the same bind port?

We instruct the OS to let us reuse the same bind port by using the socket.setsockopt() function. This function takes three parameters: the first is the socket level, the second is the socket option, and the third is the value. The socket level is SOL_SOCKET, the socket option is SO_REUSEADDR, and the value is 1.

```python
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```

## Question 4: What information do we get about incoming connections?

We get the address of the incoming connection, and the socket object that we can use to communicate with the client.

## Question 5: What is returned by recv() from the server after it is done sending the HTTP request?
The `recv()` function returns an empty byte string.

## Question 6: Provide a link to your code on GitHub.

https://github.com/qasimy123/CMPUT404Lab2