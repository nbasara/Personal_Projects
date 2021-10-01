#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include <unistd.h>
#include <pthread.h>


//shared variable
int SharedValue = 0;


/*** unAltered Code ***/

//multi threaded function for thread arguement
void SimpleThread(int thread_num) {
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
	int i, threadsToMake;

	//verify the user has given number of arguements required to run
	if(argc != 2) {
		printf("Please provide a number of threads to create.\n");
		return 0;
	}

	//Verify arguements are withing range
	int arguementLength = strlen(argv[1]);
	for(i = 0; i <arguementLength; i++) {
		if(!isdigit(argv[1][i])) {
			printf("Arguement is not a number.\n");
			return 0;
		}
	}

	threadsToMake = atoi(argv[1]);

	printf("This is the number of threads you requested.  %d\n", threadsToMake);


	//Generate that many threads
	//Send threads to SimpleThread

	return 0;
}