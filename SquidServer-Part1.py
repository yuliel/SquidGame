import socket
from consts import *

# Before
server_socket = socket.socket()
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()
print("Server is up and running")
(client_socket, client_address) = server_socket.accept()
print("Client connected")

# During

data = None
while data != EXIT_CODE:
    data = client_socket.recv(PACKET_SIZE).decode()
    print("Client sent: " + data)

    if data != EXIT_CODE:
        client_socket.send(f"{data} to you too".encode())
    else:
        client_socket.send(data.encode())

# After
client_socket.close()
server_socket.close()
