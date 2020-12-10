import socket

ClientSocket = socket.socket()
host = '192.168.0.117'
port = 8889

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response)
while True:
    Input = input('Say Something: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()

#import socket
#import os
#from _thread import *

#ServerSocket = socket.socket()
#host = '192.168.0.117'
#port = 8889
#ThreadCount = 0
#try:
#    ServerSocket.bind((host, port))
#except socket.error as e:
#    print(str(e))

#print('Waiting for a Connection..')
#ServerSocket.listen(5)

#def threaded_client(connection):
#    connection.send(str.encode('Welcome to the Server\n'))
#    while True:
#        data = connection.recv(2048)
#        reply = 'Server Says: ' + data.decode('utf-8')
#        if not data:
#            break
#        connection.sendall(str.encode(reply))
#    connection.close()

#while True:
#    Client, address = ServerSocket.accept()
#    print('Connected to: ' + address[0] + ':' + str(address[1]))
#    start_new_thread(threaded_client, (Client, ))
#    ThreadCount += 1
#    print('Thread Number: ' + str(ThreadCount))
#ServerSocket.close()

