#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	FILE * pFile;
	FILE * fd;
	//buffer = malloc(256*sizeof(char));
	char *buffer1;
	buffer1 = "CustomerID,CustomerName,ContactName,Address,City,PostalCode,Country";
	printf("buffer1 : %s\n", buffer1);
	char buffer2[256];
	strcpy(buffer2, buffer1);
	printf("buffer2 : %s\n", buffer2);
	char *buffer3;
	strcpy(buffer3, buffer2);
	printf("buffer3 : %s\n", buffer3);
	char buffer4[256];
	strcpy(buffer4, buffer3);
	printf("buffer4 : %s\n", buffer4);
	//fd = fopen("blah", "r");
	//fread (buffer, 256, 1, fd);
	//fclose(fd);
//	pFile = fopen ("myfile.bin", "w+");
//	fwrite (buffer2, 1, sizeof(buffer), pFile);
	//printf("%zu", fread(buffer, 256, 1, pFile));
//	printf("\n%s\n", buffer2);
//	fclose (pFile);
	return 0;
	//loop through the the char**
}
