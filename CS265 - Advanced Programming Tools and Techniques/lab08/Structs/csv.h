/*
 * csv.h - Interface for a csv library
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

#ifndef __KS_CSV_
#define __KS_CSV_

#include <stdio.h>

enum { NOMEM = -2 };          /* out of memory signal */

typedef struct
{
	FILE *fin ;
	char *line ;    /* input chars */
	char *sline ;   /* line copy used by split */
	int  maxline ;  /* size of line[] and sline[] */
	char **field ;  /* field pointers */
	int  maxfield ; /* size of field[] */
	int  nfield ;   /* number of fields in field[] */
}  csv_t ;

	/* return a new CSV object */
csv_t* csv_init( FILE* f ) ;

	/* read next input line */
char* csvgetline( csv_t* c ) ;

	/* return field n */
char* csvfield( csv_t* c, int n ) ;

	/* return number of fields */
int   csvnfield( csv_t* c ) ;

	/* To be called when done with an object *
	 *  Does not close the file handle */
void  kill( csv_t* c ) ;


#endif  /* __KS_CSV_ */
