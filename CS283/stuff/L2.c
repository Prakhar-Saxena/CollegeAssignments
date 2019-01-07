#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

volatile unsigned int count_g = 0;
#define N 1000

struct people{
	int* cnt;
	pthread_mutex_t* mutex;
	int id;
    // bool up = false;
};

void *count_f(void *arg){
	struct people* data = arg;
	for(int i = 0; i < N; i++){
		pthread_mutex_lock(data->mutex);
		count_g++;
		pthread_mutex_unlock(data->mutex);
	}
	return NULL;
}

// void getUp(struct people x){
//     x.up = true;
// }

int main(){
	pthread_mutex_t* lock = malloc(sizeof(pthread_mutex_t));

	pthread_mutex_init(lock, NULL);
	
	int count = 0;

	pthread_t* thread = malloc(100*sizeof(pthread_t)); //100 people
	
	struct people* x = malloc(100*sizeof(struct people)); //100 people
	
	for(int i = 1; i <= 100; i++){
		x->id = i;
		x->mutex = lock;
		x->cnt = &count;

		pthread_create(&thread[i], NULL , count_f, &x[i]);
	}

	for(int i = 1; i <= N; i++){
		pthread_join(&thread[i], NULL);
	}

//    printf("%d", count);
	

	pthread_mutex_destroy(lock);

	return 0;
}
