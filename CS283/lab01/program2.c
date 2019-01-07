#include <stdlib.h>
#include <string.h>
/*Allocate an array for 10 char* pointers. Each of the ten pointers are initialized
to an array size of 15 and each are initialized to the word 'Hello'
*/

int main() 
{
 char ** ptr = malloc(10*sizeof(char*));
 char str[] = "Hello\0";
 for(int i =0; i<10; i++)
 {
  ptr[i] = (char*)malloc(15*sizeof(char)); 
  strncpy(ptr[i], str, sizeof(ptr[i])); 
  printf("String %d: %s\n",i,ptr[i]);
 }
//De-allocate ptr after it is finished the loop 
  free(ptr);
  return 0;
}
