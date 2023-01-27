# # create a socket
# import socket

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Assign IP address and port number
# IP = "0.0.0.0"
# PORT = 8820
# server_socket.bind((IP, PORT))

# # Listen
# server_socket.listen()
# print("Server is up and running")

# # Connection to the Client
# (client_socket, client_adress) = server_socket.accept()
# print("Client connected")

# # Recieve data
# MAX_MSG_LENGTH = 1024
# data = client_socket.recv(MAX_MSG_LENGTH).decode()
# print("Client sent: " + data)

# # Send data
# client_socket.send(data.encode())

# # Disconnection from the Client
# client_socket.close()

# # Close the socket
# server_socket.close()

IP = "0.0.0.0"
PORT = 8820
MAX_MSG_LENGTH = 1024

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((IP, PORT))
server_socket.listen()
print("Server is up and running")

(client_socket, client_adress) = server_socket.accept()
print("Client connected")

while True:
    data = client_socket.recv(MAX_MSG_LENGTH).decode()
    print("Client sent: " + data)
    if (data == "Quit"):
        print("closing client socket now...")
        client_socket.send('Bye'.encode())
        break
    client_socket.send(data.encode())

client_socket.close()
server_socket.close()