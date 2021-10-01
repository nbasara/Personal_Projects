#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>


//shared variable
int SharedValue = 0;


/*** unAltered Code ***/

//multi threaded function for thread arguement
void * SimpleThread(int thread_num) {
	//individual to each thread
	//gets assigned shared value 
	int num, val;

	for(num = 0; num < 20; num++) {

		if(random() > RAND_MAX/2) usleep(500);

		val = SharedValue;

		printf("*** thread %d sees value %d\n", thread_num, val);
	
		//increment value
		SharedValue = val + 1;
	}
	val = SharedValue;
	printf("Thread %d sees value %d\n", thread_num, val);
}

/*** main thread ***/

int main(int argc, char* argv[]) {

	//Verify arguements are withing range

	//Generate that many threads
	//Send threads to SimpleThread

	return 0;
}