import socket

s = socket.socket()

ip = "192.168.0.117"
port = 5005

s.connect((ip, port))

data = s.recv(1024)

message = b'Hi, saya client.'

s.sendto(message, (ip, port));

print (data)

s.close()

