#include <stdio.h>
#include <stdlib.h>

int main() {
	FILE * pFile;
	char *buffer;
	buffer = malloc(256*sizeof(char));
	pFile = fopen ("blah", "r");
	fread (buffer, 256, 1, pFile);
	//while()
	//csaa[[ file, rio_readlineb function
//fgets should work.. //strtokr, just use strcpy	
	//size as the second parameter, 1 for 2nd parameter	
//printf("%zu", fread(buffer, sizeof(char), sizeof(buffer), pFile));
	printf("%s",buffer);
	//char *token;
	//token = strtok(buffer,',');
	//printf("%s",token);
	fclose (pFile);
	free(buffer);
	return 0;
	//loop through the the char**
}
//gcc test3.c -o test3 -fno-stack-protector
//create a linked list node, malloc char star inside the linked list node, then we strcopy into that
