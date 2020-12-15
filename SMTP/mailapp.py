from socket import *
from base64 import *
from getpass import getpass
import ssl

#The mail server and the port with SMTP chosen : Google's mail server
server = 'smtp.gmail.com'
port = 587

#The client-server application's banner
print("\n -------------------------------------------------------------------------------------------------- \n")
print("\n\n\t\t\t - CLIENT-SERVER E-MAIL APPLICATION - \n\n")
print(" \t      This python application will send your e-mail through G-mail's server. \n")
print(" \t            *Do take note that G-mail accounts are preferred.        \n")
print(" \t            *Please turn on [access for less secure apps] on \n")
print(" \t             your G-mail account to use this application. ")
print("\n -------------------------------------------------------------------------------------------------- \n")

#Sender's information fill in
print("\t\t\t PLEASE ENTER YOUR CREDENTIALS \n\n")

SENDER = input("\t\t Enter Your e-mail Address       : ")
PASSWORD = getpass("\t\t Enter Your e-mail Password      : ")

print("\n -------------------------------------------------------------------------------------------------- \n")

#Receiver's information and e-mail contents fill in
print("\t\t\t PLEASE ENTER RECEIVER's CREDENTIAL & E-MAIL CONTENTS \n\n")

RECEIVER = input("\t\t Enter Receiver's e-mail Address : ")
SUBJECT = input("\t\t Enter Subject                   : ")
MESSAGE = input("\t\t Enter Message                   : ")
ENDMESSAGE = '\r\n.\r\n'

#The process of sending the e-mail using sockets
print("\n ---------------------------- SENDING THE E-MAIL -------------------------------------------------- \n\n")

#Start SMTP connection with server (smtp.gmail.com)
socket = socket(AF_INET, SOCK_STREAM)
socket.connect((server, port))
response1 = socket.recv(1024)
print(" [+] Reply after connection request : " + response1.decode("utf-8"))

#Sending HELO/EHLO command to server to initiate SMTP conversation
cmdEHLO = 'EHLO Alice\r\n'.encode()
socket.send(cmdEHLO)
response2 = socket.recv(1024)
print(" [+] Reply after EHLO command       : " + response2.decode("utf-8"))

#Start TLS encryption
cmdSTARTTLS = "STARTTLS\r\n".encode()
socket.send(cmdSTARTTLS)
response3 = socket.recv(1024)
print(" [+] Reply after STARTTLS command   : " + response3.decode("utf-8"))

#Aunthenticating the e-mail account, to access and send e-mail
#Wrap socket with SSL to use G-mail's server securely
socketSSL = ssl.wrap_socket(socket)

SENDER_EMAIL = b64encode(SENDER.encode())
SENDER_PASSWORD = b64encode(PASSWORD.encode())

cmdAUTH = 'AUTH LOGIN\r\n'.encode()
socketSSL.send(cmdAUTH)
response4 = socketSSL.recv(1024)
print(" [+] Reply after AUTH LOGIN command : " + response4.decode("utf-8"))

socketSSL.send(SENDER_EMAIL + "\r\n".encode())
response5 = socketSSL.recv(1024)
print(" [+] Reply after sending E-MAIL     : " + response5.decode("utf-8"))

socketSSL.send(SENDER_PASSWORD + "\r\n".encode())
response6 = socketSSL.recv(1024)
print(" [+] Reply after sending PASSWORD   : " + response6.decode("utf-8"))

#Sending MAIL FROM command to server, to identify sender's e-mail
cmdMAILFROM = 'MAIL FROM: <{}>\r\n'.format(SENDER)
socketSSL.send(cmdMAILFROM.encode())
response7 = socketSSL.recv(1024)
print(" [+] Reply after MAIL FROM command  : " + response7.decode("utf-8"))

#Sending RCPT TO command to server, to identify recipient's e-mail
cmdRCPTTO = 'RCPT TO: <{}>\r\n'.format(RECEIVER)
socketSSL.send(cmdRCPTTO.encode())
response8 = socketSSL.recv(1024)
print(" [+] Reply after RCPT TO command    : " + response8.decode("utf-8"))

#Sending DATA command to server, to transfer message data
cmdDATA = 'DATA\r\n'.encode()
socketSSL.send(cmdDATA)
response9 = socketSSL.recv(1024)
print(" [+] Reply after DATA command       : " + response9.decode("utf-8"))

socketSSL.send("Subject: {}\n\n".format(SUBJECT).encode())
socketSSL.send(MESSAGE.encode())
socketSSL.send(ENDMESSAGE.encode())
response10 = socketSSL.recv(1024)
print(" [+] Reply after sending MESSAGE    : " + response10.decode("utf-8"))

#Sending QUIT command to server, to quit SMTP conversation
cmdQUIT= 'QUIT\r\n'.encode()
socketSSL.send(cmdQUIT)
response11 = socketSSL.recv(1024)
print(" [+] Reply after QUIT command       : " + response11.decode("utf-8"))

socketSSL.close()
print(" [+] Process complete. Please check your inbox. \n")
print("\n -------------------------------------------------------------------------------------------------- \n\n")

#End of application

