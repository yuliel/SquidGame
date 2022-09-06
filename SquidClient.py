import socket
from consts import *

# Before
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((SERVER_IP, SERVER_PORT))

# During
msg = None

while msg != EXIT_CODE:
    msg = input ("enter you message: ")
    my_socket.send(msg.encode())

    data = my_socket.recv(PACKET_SIZE).decode()
    print("The server sent: " + data)

# After
my_socket.close()

