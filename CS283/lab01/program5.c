#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void add(int x);

int *array;
int arraysize=20;
int elements = 100000;
int factor = 2;
int arrayelement=0;
/*main function uses clock to time program execution*/
int main() 
{
	
  clock_t start = clock();
  array = malloc(sizeof(int)*arraysize);
  for(int i = 0; i<elements; i++)
  {
    add(i);
  }
  clock_t stop = clock();
  double elapsed = (double)(stop - start) * 1000.0 / CLOCKS_PER_SEC;
  printf("Time elapsed in ms: %f", elapsed);

  return 0;
}
/*add function reallocates space so that array has one more element. Array also increase by 2 times its previous size*/
void add(int x)
{
  
 if(arrayelement >= arraysize)
 {
    int newsize = factor*arraysize+1;
    array = realloc(array, newsize*sizeof(int));
    arraysize = newsize;  
 }

 array[arrayelement] = x;
 arrayelement++;
}