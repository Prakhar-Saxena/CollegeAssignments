#include <stdio.h>

int main() {
	FILE * pFile;
	char buffer[] = { 'x' , 'y' , 'z' };
	pFile = fopen ("myfile.bin", "wb");
	fwrite (buffer, sizeof(char), sizeof(buffer), pFile);
	printf("%zu", fread(buffer, sizeof(char), sizeof(buffer), pFile));
	fclose (pFile);
	return 0;
	//loop through the the char**
}
