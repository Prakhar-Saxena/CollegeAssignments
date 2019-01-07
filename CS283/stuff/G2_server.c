int g_trace_level = BRIEF_TRACE;

int sockfd;

INT_RET main ()
{
    TRACE (BRIEF_TRACE, ("Inside main function\n"));
    struct sockaddr_in serveraddress; /*store serveraddress */
    int ret; /*store return value of bind function */
    int connfd; /*store return value of accept function */
    pthread_t th; /*store thread identification number */
    int session_no; /*store session number */
    int pthread_ret; /*store return value of pthread_create function */

    sockfd = socket (AF_INET, SOCK_STREAM, 0); /*Creating a socket for server for end point communication */
    if (-1 == sockfd) /* Error in creating socket */
    {
        TRACE (DETAILED_TRACE, ("Socket error\n"));
        perror (" Socket Error \n"); /* printing the error */
        exit (ERROR); /* exiting with error */
    }

    TRACE (DETAILED_TRACE, ("Socket has been created successfully\n"));
    serveraddress.sin_family = AF_INET; /*Address family provides interprocess communication */
    serveraddress.sin_port = htons (MY_PORT); /*Port Number of server */
    serveraddress.sin_addr.s_addr = htonl (INADDR_ANY); /*Generate the random IP address for bind */

    ret = bind (sockfd, (struct sockaddr *) &serveraddress, sizeof (serveraddress)); /*bind a name to a socket */
    if (-1 == ret) /* If there is error in binding */
    {
        TRACE (DETAILED_TRACE, ("Bind Error\n"));
        perror ("BIND"); /* print error */
        exit (FAILURE); /* exit with error */
    }

    TRACE (DETAILED_TRACE, ("Bind successfull\n"));
    listen (sockfd, 5); /*listen for connection on a socket */

    TRACE (DETAILED_TRACE, ("Listening...\n"));
    for (session_no = 0; session_no < LIST_SIZE; session_no++) /* loop for all session */
    {
        conference_list[session_no].head = NULL; /*Set conference list to null */
        FD_ZERO (&master[session_no]); /*set master list to zero */
        FD_ZERO (&read_fds[session_no]); /*set read_fds list to zero */
        fdmax[session_no] = -1;
    }

    TRACE (DETAILED_TRACE, ("Initializing all lists\n"));

    while (1) /*for communicating to others clients concurrently */
        {
        printf ("Waiting for client............\n");
        connfd = accept (sockfd, (struct sockaddr *) NULL, NULL); /*accept a connection on a socket */

        if (-1 == connfd) /* error in accept call */
        {
            TRACE (DETAILED_TRACE, ("error in accept call\n"));
            if (EINTR == errno) /* if error is of type EINTR */
            perror ("Interrupted system call??");
            continue;
        }

        TRACE (DETAILED_TRACE, ("Client has been accepted successfully\n"));
        pthread_ret = pthread_create (&th, NULL, conn_client_entry_handler, (void *) &connfd); /*creating a thread for defferent clients */

        TRACE (DETAILED_TRACE, ("Thread is created to handle client\n"));
        if (0 != pthread_ret) /* if there is error in creating thread */
        {
            TRACE (DETAILED_TRACE,
            ("Error in creating thred forn handlin client\n"));
            perror ("ERROR:IN CREATING THREAD\n"); /* print error */
        }
    }
    pthread_exit (NULL);
}