#include<stdio.h> 
#include<netdb.h> 
#include<netinet/in.h> 
#include<stdlib.h> 
#include<string.h> 
#include<sys/socket.h> 
#include<sys/types.h> 
#include<arpa/inet.h>
#include<unistd.h>
  
// Function for Client and Server chat
void chat(int socket_desc) 
{ 
    char message[100]; 
    int n; 

    // infinite loop for chat 
    for (;;) 
    { 
        bzero(message, sizeof(message)); 
  
        // Read the message from client and copy it 
        read(socket_desc, message, sizeof(message));

        // Print message which contains the client contents 
        printf("From Client: %s \t To Client : ", message); 
        bzero(message, sizeof(message)); 
        n = 0; 

        // Copy server message  
        while ((message[n++] = getchar()) != '\n'); 
  
        // Send that copy to client 
        write(socket_desc, message, sizeof(message)); 
  
        // If message contains "Exit" then server exit and chat ended. 
        if (strncmp("exit", message, 4) == 0) 
        { 
            printf(" - Server Exit - \n"); 
            break; 
        } 
    } 
} 
  
int main() 
{ 
    int socket_desc, new_socket, c; 
    struct sockaddr_in server, client; 

    printf(" \n - SERVER -\n\n");
  
    // Create socket
    socket_desc = socket(AF_INET, SOCK_STREAM, 0); 

    if (socket_desc == -1) 
    { 
       printf("Could not create socket \n"); 
        exit(0); 
    } 
    else
        printf("Socket successfully created \n");

    bzero(&server, sizeof(server)); 

    server.sin_family = AF_INET; 
    server.sin_addr.s_addr = htonl(INADDR_ANY); 
    server.sin_port = htons( 8888 ); 
  
    // Binding newly created socket to given IP and verification 
    if ((bind(socket_desc, (struct sockaddr *)&server, sizeof(server))) != 0) 
    { 
        printf("Socket bind failed \n"); 
        exit(0); 
    } 
    else
        printf("Socket successfully binded \n"); 
  
    // Now server is ready to listen and verification 
    if ((listen(socket_desc, 5)) != 0) 
    { 
        printf("Listen failed \n"); 
        exit(0); 
    } 
    else
        printf("Server is now listening \n");

    c = sizeof(client); 
  
    // Accept the data packet from client and verification 
    new_socket = accept(socket_desc, (struct sockaddr *)&client, &c); 

    if (new_socket < 0) 
    { 
        printf("Server acccept failed \n"); 
        exit(0); 
    } 
    else
        printf("Server acccepts Client \n\n"); 
  
    // Function for chatting between client and server
    printf("[ SERVER - CLIENT CHAT SESSION ] \n\n"); 
    chat(new_socket); 
  
    // After chatting close the socket 
    close(socket_desc); 

    return 0;
} 
