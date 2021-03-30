#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void *myThreadFun(void *vargp){
	sleep(1);
	printf("Printing from thread \n");
	return NULL;
}

int main(){
	pthread_t thread_id;
	printf("before\n");
	pthread_create(&thread_id, NULL, myThreadFun, NULL);
	pthread_join(thread_id, NULL);
	printf("after\n");
	exit(0);
}
