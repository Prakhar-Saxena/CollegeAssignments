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


//---------------------------------------------------------------------------------
//SERVER

#include <stdio.h>
#include "csapp.h"

int main(int argc, char **argv){
    int listenfd, connfd, port, clientlen;
    struct sockaddr_in clientaddr;
    struct hostent *hp;
    char *haddrp;

    port = atoi(argv[1]);

    listenfd = open_listenfd(port);

    while(1){
        clientlen = sizeof(clientaddr);
        connfd = Accept(listenfd, (SA *)&clientaddr, &clientlen);
        hp = Gethostbyaddr((const char *)&clientaddr.sin_addr.sin_addr, /*not sure if sin_addr.sin_addr OR sin_addr.s_addr*/ sizeof(clientaddr.sin_addr.s_addr), AF_INET);
        haddrp = inet_ntoa(clientaddr.sin_addr);
        printf("server connected to %s (%s)\n", hp->h_name, haddrp);
        echo(connfd);
        Close(connfd);
    }
}

int open_listenfd(int port){
    int listenfd, optval=1;
    struct sockaddr_in serveraddr;
    if((listenfd = socket(AF_INET, SOCK_STREAM, 0)) < 0){
        return -1;
    }

    if(setsockopt(listenfd, SOL_SOCKET, SO_REUSEADDR, (const void *)&optval, sizeof(int)) < 0){
        return -1;
    }

    bzero((char *) &serveraddr, sizeof(serveraddr));
    serveraddr.sin_family = AF_INET;
    serveraddr.sin_addr.sin_addr = htonl(INADDR_ANY);
    serveraddr.sin_port = htons((unsigned short) port);
    if(bind(listenfd, (SA*)&serveraddr, sizeof(serveraddr)) < 0){
        return -1;
    }

    return listenfd;
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
