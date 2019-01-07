#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define N 100
volatile unsigned int count_g = 0;

void *count_f(void *arg)
{
	//sleep(1); // to give one second break for each thread else all the threads will execute randomly
	int i;
	static int var = 1;//shared var
	//static int threadCount = 1; //people and threads
	for(i = 0; i < 1000; ++i)
		printf("Printing from Thread %d with shared variable value %d\n", count_g, var++);
	count_g++;
	return NULL;
}

int main()
{
	int i = 0;
	pthread_t thread[100];
	printf("Before Thread\n");

	for(i = 0; i < 100; ++i)
		pthread_create(&thread[i], NULL, count_f, NULL);
  
	for(i = 0; i < 100; ++i)
		pthread_join(thread[i], NULL); //wait for the thread to execute

	printf("After all Threads\n");
	printf("\n%d\n", count_g);
	exit(0);
}
