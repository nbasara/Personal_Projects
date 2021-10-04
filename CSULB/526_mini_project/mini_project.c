#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include <unistd.h>
#include <pthread.h>


//shared variable
int SharedValue = 0;

//mutex lock
pthread_mutex_t lock;

//barrier
pthread_barrier_t barrier;


/*** unaltered Code ***/

//multi threaded function for thread arguement
/*
void * SimpleThread(void * which) {
	//individual to each thread
	//gets assigned shared value 
	int num, val;

	int thread_num = *(int *) which;

	for(num = 0; num < 20; num++) {

		if(random() > RAND_MAX/2) usleep(500);

		val = SharedValue;

		printf("*** thread %d sees value %d\n", thread_num, val);
	
		//increment value
		SharedValue = val + 1;
	}
	val = SharedValue;
	printf("Thread %d sees final value %d\n", thread_num, val);
}
*/


/*** alterered code ***/
//which is an integer pointer to where each thread number is stored
void * SimpleThread(void * which) {
	int num, val;
	int thread_num = *(int *) which;


	for(num = 0; num < 20; num++) {
		#ifdef PTHREAD_SYNC
		pthread_mutex_lock(&lock);
		#endif 
		val = SharedValue;

		printf("*** thread %d sees value %d\n", thread_num, val);
		SharedValue = val + 1;
		#ifdef PTHREAD_SYNC
		pthread_mutex_unlock(&lock);
		#endif 
	}
	//barrier here
	#ifdef PTHREAD_SYNC
	pthread_barrier_wait(&barrier);
	#endif

	val = SharedValue;
	printf("Thread %d sees final value %d\n", thread_num, val);


}


/*** main thread ***/

//given two arguements program_name, threads to make
int main(int argc, char* argv[]) {
	int i, threadsToMake, error;

	//verify the user has given number of arguements required to run
	if(argc != 2) {
		printf("Please provide a number of threads to create.\n");
		return 0;
	}

	//Verify arguements are within range - integer
	int arguementLength = strlen(argv[1]);
	for(i = 0; i <arguementLength; i++) {
		if(!isdigit(argv[1][i])) {
			printf("Arguement is not a number.\n");
			return 0;
		}
	}
	//convert arguement to integer
	threadsToMake = atoi(argv[1]);

	//Making an array of pthreads
	pthread_t thread_array[threadsToMake];
	//makingan array of thread_nums to pass to function
	int thread_nums[threadsToMake];
	//initialize barrier to the number of threads for program
	pthread_barrier_init(&barrier, NULL, threadsToMake);

	for(i = 0; i < threadsToMake; i++){
		//store the thread numbers
		thread_nums[i] = i;

		//Generate that many threads
		//Send threads to SimpleThread
		error = pthread_create(&thread_array[i], NULL, SimpleThread, (void *) &thread_nums[i]);
		if(error != 0){
			printf("Problem creating thread %d", i);
			return 0;
		}
	}

	//join all threads
	for(i = 0; i < threadsToMake; i++){
		pthread_join(thread_array[i], NULL);
	}

	return 0;
}