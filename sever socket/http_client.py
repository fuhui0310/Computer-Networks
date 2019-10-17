# Fu Hui
# 94308158

# import socket module
from socket import *
import sys

# The socket module forms the basis of all network communication
comment = sys.argv[1:]

# Server name: Can be IP or name (e.g. "128.138.32.126" or "yourserver.eng.uci.edu")
serverName = comment[0]

# Specify port
serverPort = int(comment[1])

# Create socket for communication
# AF_INET specifies address family which is IPv4
# SOCK_STREAM shows the protocol for the socket which is TCP here.
clientSocket = socket(AF_INET, SOCK_STREAM)

# Initiate the TCP connection (3-way handshake completes after this line is done)
clientSocket.connect((serverName, serverPort))

# Ask user for input string
message = "GET /" + comment[2] + " HTTP/1.1\r\n"

# Convert sentence to bytes and send to the server
clientSocket.send(message.encode())

# Wait for a response from the server (max 1024 bytes)
response = clientSocket.recv(1024)

# Print the response and close the socket
print(response.decode())

while response.decode() != "":
    # Wait for a response from the server (max 1024 bytes)
    response = clientSocket.recv(1024)

    # Print the response and close the socket
    print(response.decode())


clientSocket.close()
