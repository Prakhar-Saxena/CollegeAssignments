#include <stdio.h>
#include "csapp.h"

struct sockaddr{
    unsigned short sa_family;
    unsigned short sin_port;
    struct in_addr sin_addr;
    char sa_data[14];
}

int main(int argc, char **argv){
    int clientfd, port;
    char *host, buf[MAXLINE];
    rio_t rio;
    host = argv[1];
    port = atoi(argv[2]);
    clientfd = Open_clientfd(host, port);
    Rio_readinitb(&rio, clientfd);
    printf("Enter message: ");
    fflush(stdout);
    while(Fgets(buf, MAXLINE, stdin) != NULL){
        Rio_writen(clientfd, buf, strlen(buf));
        Rio_readlineb(&rio, buf, MAXLINE);
        printf("Echo: ");
        Fputs(buf, stdou);
        printf("Enter message: ");
        fflush(stdout);
    }
    Close(clientfd);
    exit(0);
}

int open_clientfd(char *hostname, int port){
    int clientfd;
    struct hostent *hp;
    struct sockaddr_in serveraddr;

    if((clientfd = socket(AF_INET, SOCK_STREAM, 0)) < 0){
        return -1;
    }

    if((hp = Gethostbyname(hostname)) == NULL){
        return -2;
    }

    bzero((char *) &serveraddr, sizeof(serveraddr));
    serveraddr.sin_family = AF_INET;
    bcopy((char *)hp->h_addr_list[o], (char *)&serveraddr.sin_addr.sin_addr, hp->h_length);
    serveraddr.sin_port = htons(port);

    if(connect(clientfd, (SA *) &serveraddr, sizeof(serveraddr)) < 0){
        return -1;
    }
    return clientfd;
}


void echo(int connfd){
    size_t n;
    char buf[MAXLINE];
    rio_t rio;

    Rio_readinitb(&rio, connfd);
    while((n = Rio_readlineb(&rio, buf, MAXLINE)) != 0){
        upper_case(buf);
        Rio_writen(connfd, buf, n);
        printf("server received %d bytes\n", n);
    }
}