#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> 
#include <sys/socket.h>
#include <sys/stat.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <string.h>
#include <fcntl.h>
#include <errno.h>

//int numThread = 4;
pthread_t       myThread;
pthread_mutex_t tLock;
pthread_cond_t  tCond;	

//this worked
/*
void * gotoSleep(){
	printf("\tThe thread is going to sleep\n");
	pthread_mutex_lock(&tLock);
	pthread_cond_wait(&tCond, &tLock);
	pthread_cond_signal(&tCond);
	pthread_mutex_unlock(&tLock);
	printf("\tThe Thread is awake and returning to main\n");
	return NULL;

}*/

int main (){

	//Run this loop forever
	int count = 0;
	while(count < 5){
		printf("Waking the thread\n");
		pthread_mutex_lock(&tLock);
		pthread_cond_wait(&tCond, &tLock);
		pthread_cond_signal(&tCond);
		pthread_mutex_unlock(&tLock);
		pthread_create(&myThread, NULL, gotoSleep, NULL);
		printf("Hopefully the thread is done!!!\n");
		count++;
	}


	return 0;
}


