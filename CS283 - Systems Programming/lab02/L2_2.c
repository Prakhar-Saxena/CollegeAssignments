#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define N 100
volatile unsigned int count_g = 0;

struct people{
	int* cnt;
	pthread_mutex_t* mutex;
	int id;
};

void *count_f(void *arg)
{
	//sleep(1); // to give one second break for each thread else all the threads will execute randomly
	int i;
	static int var = 1;//shared var
	//static int threadCount = 1; //people and threads
	for(i = 0; i < 1000; ++i){
		pthread_mutex_lock(arg->mutex);
		printf("Printing from Thread %d with shared variable value %d\n", count_g, var++);
		pthread_mutex_unlock(arg->mutex);
	}
	count_g++;
	return NULL;
}

int main()
{
	pthread_mutex_t* lock = malloc(sizeof(pthread_mutex_t));
	pthread_mutex_init(lock, NULL);
	
	int i = 0;
	pthread_t thread[100];
	printf("Before Thread\n");
	
	struct people* x = malloc(100*sizeof(struct people));
	
	
	for(i = 0; i < 100; ++i){
		x[i].id = i;
		x[i].mutex = &lock;
		x[i].cnt = count_g;
		pthread_create(&thread[i], NULL, count_f, NULL);
	}

	for(i = 0; i < 100; ++i){
		pthread_join(thread[i], NULL); //wait for the thread to execute
	}

	printf("After all Threads\n");
	printf("\n%d\n", count_g);
	
	pthread_mutex_destroy(lock);
	exit(0);
}
