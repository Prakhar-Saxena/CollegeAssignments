/*
 * main.c - Driver for the csv library
 *
 * Modified from code in Kernighan & Pike, _The Practice of Programming_
 *   Copyright (C) 1999 Lucent Technologies 
 *   Excerpted from 'The Practice of Programming' 
 *   by Brian W. Kernighan and Rob Pike 
 *
 * Kurt Schmidt
 * 3/2018
 *
 * gcc 5.4.0 20160609 on
 * Linux 4.13.0-32-generic
 *
 * EDITOR:  tabstop=2 cols=120
 */

#include <stdio.h>
#include <stdlib.h>
#include "csv.h"


int main( int argc, char** argv )
{
	int i ;
	char *line ;
	FILE *f = NULL ;
	csv_t *c1 = NULL ;

	if( argc==1 )
		f = stdin ;
	else
		f = fopen( argv[1], "r" ) ;

	c1 = csv_init( f ) ;

	while( (line=csvgetline( c1 )) != NULL )
	{
		printf( "line: %s\n", line ) ;
		for( i=0; i < csvnfield(c1); i++ )
			printf( "  field[%d]: %s\n", i, csvfield( c1, i )) ;
	}

	return 0;
}

