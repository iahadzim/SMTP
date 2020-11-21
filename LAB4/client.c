
#include<netdb.h> 
#include<stdio.h> 
#include<stdlib.h> 
#include<string.h> 
#include<sys/socket.h>
#include<arpa/inet.h> 
#include<unistd.h>

void chat(int socket_desc) 
{ 
    char message[100]; 
    int n; 
    for (;;) 
    { 
        bzero(message, sizeof(message)); 
        printf("Enter message : "); 
        n = 0; 
        while ((message[n++] = getchar()) != '\n');

        write(socket_desc, message, sizeof(message)); 
        bzero(message, sizeof(message));

        read(socket_desc, message, sizeof(message)); 
        printf("\t From Server : %s", message);

        if ((strncmp(message, "exit", 4)) == 0) 
        { 
            printf(" - Client Exit - \n"); 
            break; 
        } 
    } 
} 
  
int main() 
{ 
    int socket_desc;
    struct sockaddr_in server; 

    printf(" \n - CLIENT -\n\n");

    // Create socket
    socket_desc = socket(AF_INET, SOCK_STREAM, 0); 
    if (socket_desc == -1) { 
        printf("Could not create socket \n");
        exit(0); 
    } 
    else
        printf("Socket successfully created \n");

    bzero(&server, sizeof(server)); 
  
    server.sin_family = AF_INET; 
    server.sin_addr.s_addr = inet_addr("192.168.0.117"); 
    server.sin_port = htons( 8888 ); 
  
    // Connect the Client socket to Server socket 
    if (connect(socket_desc, (struct sockaddr *)&server, sizeof(server)) != 0) 
    { 
        printf("Connection to server failed \n"); 
        exit(0); 
    } 
    else
        printf("Connected to the server..\n\n"); 
  
    // Chat function 
    printf("[ CLIENT - SERVER CHAT SESSION ] \n\n");
    chat(socket_desc); 
   
    close(socket_desc); 

    return 0;
} 
