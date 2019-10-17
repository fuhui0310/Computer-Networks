# Fu Hui
# 94308158

# import socket module
from socket import *
from _thread import *


# create thread function
def thread(connectionSocket, addr):

    try:
        # Fill in start
        message = connectionSocket.recv(1024)
        # Fill in end
        message_split = message.split()
        if len(message_split) <= 1:
            # Small connection from browser - ignore
            connectionSocket.close()
        filename = message_split[1]
        f = open(filename[1:], 'rb')
        outputdata = f.read()

        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send("\nHTTP/1.1 200 OK\n\n".encode())
        # Fill in end

        # Send the content of the requested file to the client
        # Fill in start
        connectionSocket.send(outputdata)
        connectionSocket.send("\r\n".encode())
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end
    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send("\nHTTP/1.1 404 Not Found\n\n".encode())
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end


def Main():
    # create an IPv4 TCP socket
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a sever socket
    serverSocket.bind(("localhost", 6789))

    # Listen for connections from client
    serverSocket.listen(5)

    while True:
        # Establish the connection
        print("Ready to serve...")
        # Fill in start
        connectionSocket, addr = serverSocket.accept()
        # Fill in end
        # create a new thread from which to serve that client
        start_new_thread(thread, (connectionSocket, addr))

    serverSocket.close()


if __name__ == '__main__':
    Main()
