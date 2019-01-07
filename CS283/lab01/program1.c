#include <stdlib.h>

/*Define a pointer X to an integer and create an array of 10 integers and populate
the array with values*/

int main() 
{
 int* X = malloc(10 * sizeof *X);
 for(int i =0; i<10; i++)
 {
    X[i]=i*i;
    printf("%d ",X[i]);
 }
 //After all values in array are filled with values, we de-allocate the pointer
 free(X);

 return 0;
}