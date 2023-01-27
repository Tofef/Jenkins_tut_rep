# # create a socket
# import socket

# my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Connect to the server
# IP = "127.0.0.1"    # Local Host
# PORT = 8820 
# my_socket.connect((IP, PORT))

# # Send data
# my_socket.send("hello".encode())

# # Recieve data
# MAX_MSG_LENGTH = 1024
# data = my_socket.recv(MAX_MSG_LENGTH).decode()
# print("The server sent: " + data)

# # Close the socket
# my_socket.close()

IP = "127.0.0.1"    # Local Host
PORT = 8820 
MAX_MSG_LENGTH = 1024

import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_socket.connect((IP, PORT))

data = ""
while (data != "Bye"):
    msg = input("Please input your message:\n")
    my_socket.send(msg.encode())
    data = my_socket.recv(MAX_MSG_LENGTH).decode()
    print("The server sent: " + data)

my_socket.close()