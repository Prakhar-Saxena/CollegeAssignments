/*********************************************************************
 * core-eg.c - example of using coredump for backtrace after crash
 *
 * Kurt Schmidt
 * 12/11
 *
 * gcc version 4.4.5 (Ubuntu/Linaro 4.4.4-14ubuntu5) 
 * Linux 2.6.35-30-generic #61-Ubuntu SMP Tue Oct 11 17:52:57 UTC 2011
 * 	x86_64 GNU/Linux
 *
 * EDITOR:  tabstop=2, cols=80
 *
 *********************************************************************/

#include <stdio.h>

int blah( int n )
{
	printf( "blah> entry\n" );
	return n / 0 ;
}

int bar( int n )
{
	printf( "bar> entry\n" );
	return blah( n+5 );
}

int foo( int n )
{
	printf( "foo> entry\n" );
	return bar( 3*n );
}

int main()
{
	printf( "main> entry\n" );

	foo( 27 ) ;

	return( 0 ) ;
}
