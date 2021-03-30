#include <stdlib.h>
#include <stdio.h>

struct ListNode
{
int value;
struct ListNode *next;
};

int main() 
{
 int arr[] = {13, 49, 34, 68, 76, 12, 4, 98};
 int sizeOfArray = 8;
 //Lined list starts off empty
 struct ListNode *start = NULL;
 /* create linked list from array */
 for(int i = 0; i<sizeOfArray; i++)
 {
  insert(&start, arr[i]);
 }
 sort(start);
 return 0;
}

/*Function to insert a node at the beginning of a linked list */
int insert(struct ListNode **start, int value)
{
  struct ListNode *ptr = (struct ListNode*)malloc(sizeof(struct ListNode));
  ptr->value = value;
  ptr->next = *start;
  *start = ptr;
}
/* BubbleSort used to sort linked list */
int sort(struct ListNode *start){
  int i, swapped;
  struct ListNode *ptr1;
  struct ListNode *ptr2 = NULL;
  if (start == NULL)
  {
  return;
  }
  do 
  {
    swapped = 0;
    ptr1= start;    
    while(ptr1->next != ptr2)
    {
      if (ptr1->value > ptr1->next->value)
      {
        swap(ptr1, ptr1->next); 
        swapped = 1;
      }
      ptr1 = ptr1->next;
    }
    ptr2=ptr1;   
    struct ListNode *temp = start;
    printf("\n");
    while (temp!=NULL)
    {
        printf("%d ", temp->value);
        temp = temp->next;
    }  
  }
  while(swapped);
}
/*swap function swaps actual nodes and not just the values of those nodes*/
void swap(struct ListNode *a, struct ListNode *b)
{
    int temp = a->value;
    a->value = b->value;
    b->value = temp;
}
