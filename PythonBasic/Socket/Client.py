#Clinet Socket
import socket

s = socket.socket()

host = "WANYICHE3"
port = 1234

s.connect((host, port))
print(s.recv(1024))
