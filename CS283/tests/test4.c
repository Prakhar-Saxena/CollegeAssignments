#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	FILE * pFile;
	char *buffer;
	const char nl[2] = "\n";
	buffer = malloc(256*sizeof(char));
	pFile = fopen ("blah", "r");
	fread (buffer, 256, 1, pFile);
//	printf("%s",buffer);
	char *token;
	token = strtok(buffer, nl);
	while(token != NULL){
		printf("%s\n",token);
		token = strtok(NULL, nl);
	}
	fclose (pFile);
	free(buffer);
	return 0;
}
