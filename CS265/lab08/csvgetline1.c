/* Copyright (C) 1999 Lucent Technologies */
/* Excerpted from 'The Practice of Programming' */
/* by Brian W. Kernighan and Rob Pike */
/*
 * EDITOR:  cols=80, tabstop=2
 *
 * Modified:
 *	DEC 2015, K Schmidt
 *	- pulled it all into one file (for demo purposes)
 *	- changed formatting a wee bit
 */

#include <stdio.h>
#include <string.h>

char buf[200];		/* input line buffer */
char* field[20];	/* fields */
char* unquote( char* );

	/* csvgetline: read and parse line, return field count */
	/* sample input: "LU",86.25,"11/4/1998","2:19PM",+4.0625,"abc" */
int csvgetline( FILE* fin )
{	
	int nfield ;
	char *p, *q ;

	if( fgets( buf, sizeof( buf ), fin ) == NULL )
		return -1 ;
	nfield = 0 ;
	for( q=buf; (p=strtok( q, ",\n\r" ))!=NULL; q=NULL )
		field[nfield++] = unquote(p) ;
	return nfield ;
}

	/* unquote: remove leading and trailing quote */
char* unquote( char *p )
{
	if( p[0] == '"' ) {
		if( p[strlen(p)-1] == '"' )
			p[strlen(p)-1] = '\0' ;
		p++ ;
	}
	return p ;
}

int main( int argc, char* argv[] )
{
	int i, nf ;
	FILE* fp ;

	if( argc < 2 ) 
		fp = stdin ;
	else
		fp = fopen( argv[1], "r" ) ;

	while(( nf=csvgetline( fp )) != -1 )
	{
		for( i=0 ; i<nf ; i++ )
			printf( "field[%d] = %s\n", i, field[i] ) ;
		printf( "\n" ) ;
	}

	return 0 ;
}

