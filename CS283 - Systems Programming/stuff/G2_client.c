int g_trace_level = DETAILED_TRACE;


INT_RET
main (IN int argc, IN char *argv[])
{
    TRACE (BRIEF_TRACE, ("Inside main function\n"));
    char rec_buff[BUFFER_SIZE]; /* stores the data recieved by the client */
    char user[INFO_SIZE]; /* stores the name of the user */
    int sockfd; /* socket descriptor */
    int fdmax, i; /* stores the maximum descriptor */
    struct sockaddr_in serveraddress; /* structur of typr sockaddr_in */
    fd_set master; /* master list */
    fd_set read_fds; /* list of read descriptors */
    int ret; /* stores return value */
    char send_buf[INFO_SIZE]; /* stores data to be send to other end */

    memset (rec_buff, '\0', BUFFER_SIZE); /* intializing recieve buffer with \0 */
    memset (user, '\0', INFO_SIZE); /* initializing user with \0 */

    if (NULL == argv[1]) /* if IP address is not provided of the server is not provided */
    {
        TRACE (DETAILED_TRACE, ("IP address is not provided\n"));
        printf ("Please provide IP address of the server\n");
        exit (0); /* exiting */
    }

    if (NULL == argv[2]) /* if port number at which server is running is not provided */
    {
        TRACE (DETAILED_TRACE, ("Port number is not provided\n"));
        printf ("Please provide port no of server\n");
        exit (0); /* exiting */
    }

    sockfd = socket (AF_INET, SOCK_STREAM, 0); /* socket descriptor is created using socket function */

    if (ERR_STATUS == sockfd) /* if error in creating socket */
    {
        TRACE (DETAILED_TRACE, ("Error in creating socket\n"));
        perror ("Socket Error");
        exit (ERROR); /* exit with error */
    }
    TRACE (DETAILED_TRACE, ("Socket has been created successfully\n"));

    serveraddress.sin_family = AF_INET; /* specifying the family as IPv4 */
    serveraddress.sin_port = htons (atoi (argv[2])); /* setting the port field of structure */
    serveraddress.sin_addr.s_addr = inet_addr (argv[1]); /* setting the address field of structure */

    ret = connect (sockfd, (struct sockaddr *) &serveraddress, /* connecting to the server */
    sizeof (serveraddress));

    if (ERR_STATUS == ret) /* error in connecting to server */
    {
        TRACE (DETAILED_TRACE, ("Error in connecting to socket\n"));
        perror ("Connect Error");
        exit (ERROR); /* exiting with error */
    }

    TRACE (DETAILED_TRACE, ("Connection is successfully done \n"));
    FD_ZERO (&master); /* initializing the master list with 0 */
    FD_ZERO (&read_fds); /* initializing the read_fd list with 0 */
    FD_SET (0, &master); /* setting the master list with descriptor of stdin */
    FD_SET (sockfd, &master); /* setting the master list with socket descriptor */
    fdmax = sockfd; /* setting the fdmax with the descriptor value of sockfd */

    TRACE (DETAILED_TRACE,
    ("Calling client_registration_And_Authentication function\n"));
    conn_client_registration_and_authentication (sockfd, user, rec_buff); /* calling function to register or authenticate client */
    printf ("%s\n", rec_buff); /* printing data recieved by client */

    if (strcmp (rec_buff, "INVALID") == 0) /* if client is invalid */
    {
        TRACE (DETAILED_TRACE, ("Invalid username and password\n"));
        printf ("Invalid Username and Password\n");
        exit (0); /* exit from system */
    }

    if (strcmp (user, "ADMIN") == 0) /* if client is identified as administrator */
    {
        TRACE (DETAILED_TRACE, ("User is identified as administrator\n"));
        printf ("Welcome administrator......\n");
        TRACE (DETAILED_TRACE, ("Calling admin_operation function\n"));
        conn_admin_operation (sockfd); /* calling function to handle administartor */
    }

    else /* if client is not an administartor */
    {
        TRACE (DETAILED_TRACE, ("%s is validated", user));
        memset (send_buf, '\0', INFO_SIZE); /* initializing send buffer with \0 */
        TRACE (DETAILED_TRACE, ("Calling choice_for_conference function\n"));
        conn_choice_for_conference (sockfd); /* calling the function to as for choice of conference */
        // user[strlen (user) - 1] = '\0';   
        sleep (1); /* for synchronization */
        strcpy (send_buf, user); /* copying user name into buffer */
        strcat (send_buf, " has joined conversation\n");
        wrap_write_to_socket (sockfd, send_buf); /* writing to socket about joining of conversation */
        while ('\n' != getchar ()); /* claering the input buffer */

        TRACE (DETAILED_TRACE, ("Entering while loop\n"));
        while (1)
        {
            read_fds = master; /* setting read_fds with master list */
            TRACE (DETAILED_TRACE, ("Waiting for select command to unblock\n"));
            select (fdmax + 1, &read_fds, NULL, NULL, NULL); /* select command */
            TRACE (DETAILED_TRACE, ("Outside select command\n"));
            for (i = 0; i <= fdmax; i++) /* when there is some data to read or write by client */
            {
                if (FD_ISSET (i, &read_fds)) /* identifying which descriptor is set */
                {
                    TRACE (DETAILED_TRACE,
                    ("calling communicate_with_other_clients function\n"));
                    conf_communicate_with_other_clients (i, sockfd, user); /* calling function to raed or wrote data to other clients */
                }
            }
        }
    }
    return 0;
}