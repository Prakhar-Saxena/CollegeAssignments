#include <stdlib.h>
#include <stdio.h>

int main() {
 int size = 16;
    int *array = (int *) malloc(size * sizeof(int));
    array[0] = 7;
    array[1] = 6;
    array[2] = 9;
    array[3] = 3;
    array[4] = 34;
    array[5] = 56;
    array[6] = 49;
    array[7] = 26;
    int sizeOfArray = 8;
    sort(array, sizeOfArray);
  return 0;
}

//BubbleSort is the sorting method used 
int sort(int *a, int size)
{
  int i, j, temp;
  for(i = 0; i < size; i++)
  {
    for(j = i + 1; j < size; j++)
    {
      if( *(a+i) > *(a+j) )
      {
        temp = *(a+i);
        *(a+i) = *(a+j);
        *(a+j) = temp;
      }
    }    
  }
  printf("Sorted array (ascending) is:\n");
    for (i=0; i<size; i++)
    {
        printf("%d ",*(a+i));
    }
    printf("\n");
    return 0;
}

