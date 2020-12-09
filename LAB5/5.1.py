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


#import socket

#s = socket.socket()
#print("Berjaya buat sokett")

#port = 5005
#ip = "192.168.0.117"

#s.bind((ip, port))
#print("Berjaya bind soket di port: " + str(port))

#s.listen(5)
#print("soket tengah menunggu client!")

#message = b'Thank you'

#while True:
#       c, addr = s.accept()
#        print("Dapat capaian dari: " + str(addr))
#
#        c.sendto(message, (ip, port))
#        buffer = c.recv(1024)
#        print(buffer)
#c.close()


