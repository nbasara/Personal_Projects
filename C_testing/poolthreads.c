#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

#include "poolthreads.h"

// going to redevelop a linked list in order to get the
// pool of threads working

// using tutorial Thread pool C John's Blog

// not sure what this is for just yet
struct tpool_work {
    int               *arg;  // argument needed for function call
    struct tpool_work *next; // points to the next work need to be done
};
typedef struct tpool_work tpool_work_t;

struct tpool {
    tpool_work_t    *work_first;   // first item in queue
    tpool_work_t    *work_last;    //
    pthread_mutex_t  work_mutex;   // lock for work to be done
    pthread_cond_t   work_cond;    // cond for work to be processed
    pthread_cond_t   working_cond; // no threads processing
    size_t           working_cnt;  // amount threads working
    size_t           thread_cnt;   // amount of active threads 
};

// add a job to the queue 
static tpool_work_t *tpool_work_create(thread_func_t func, void *arg)
{
    tpool_work_t *work;

    if (func == NULL)
        return NULL;

    work       = malloc(sizeof(*work));
    work->func = func;
    work->arg  = arg;
    work->next = NULL;
    return work;
}

// job is done/passed off destroy and free memory
static void tpool_work_destroy(tpool_work_t *work)
{
    if (work == NULL)
        return;
    free(work);
}

//
static tpool_work_t *tpool_work_get(tpool_t *tm)
{
    tpool_work_t *work;

    if (tm == NULL)
        return NULL;

    work = tm->work_first;
    if (work == NULL)
        return NULL;

    if (work->next == NULL) {
        tm->work_first = NULL;
        tm->work_last  = NULL;
    } else {
        tm->work_first = work->next;
    }

    return work;
}

// the func value will not be needed
// will just call handle client
// arg will be client socket
static void *tpool_worker(void *arg)
{
    tpool_t      *tm = arg; //work to do
    tpool_work_t *work;     //work queue

    while (1) {
        pthread_mutex_lock(&(tm->work_mutex));

        while (tm->work_first == NULL)
            pthread_cond_wait(&(tm->work_cond), &(tm->work_mutex));


        work = tpool_work_get(tm); //get work from the working queue
        tm->working_cnt++; // one more thread is working
        pthread_mutex_unlock(&(tm->work_mutex)); // Allow someone else to change

        if (work != NULL) {
            work->func(work->arg); // do work  change to handle client
            tpool_work_destroy(work); // destroy work just did
        }

        pthread_mutex_lock(&(tm->work_mutex));
        tm->working_cnt--;
        if (tm->working_cnt == 0 && tm->work_first == NULL)
            pthread_cond_signal(&(tm->working_cond));
        pthread_mutex_unlock(&(tm->work_mutex));
    }

    tm->thread_cnt--;
    pthread_cond_signal(&(tm->working_cond));
    pthread_mutex_unlock(&(tm->work_mutex));
    return NULL;
}

//creates the thread and makes them wait until there is work to do
//call this before the while(true)
tpool_t *tpool_create(size_t num)
{
    tpool_t   *tm;
    pthread_t  thread;
    size_t     i;

    if (num == 0)
        num = 2;

    tm             = calloc(1, sizeof(*tm));
    tm->thread_cnt = num;

    pthread_mutex_init(&(tm->work_mutex), NULL);
    pthread_cond_init(&(tm->work_cond), NULL);
    pthread_cond_init(&(tm->working_cond), NULL);

    tm->work_first = NULL;
    tm->work_last  = NULL;

    for (i=0; i<num; i++) {
        pthread_create(&thread, NULL, tpool_worker, tm);
        pthread_detach(thread);
    }

    return tm;
}

//adding work to the queue
//this function goes in with accept
bool tpool_add_work(tpool_t *tm, thread_func_t func, void *arg)
{
    tpool_work_t *work;

    if (tm == NULL)
        return false;

    work = tpool_work_create(func, arg);
    if (work == NULL)
        return false;

    pthread_mutex_lock(&(tm->work_mutex));
    if (tm->work_first == NULL) {
        tm->work_first = work;
        tm->work_last  = tm->work_first;
    } else {
        tm->work_last->next = work;
        tm->work_last       = work;
    }

    pthread_cond_broadcast(&(tm->work_cond));
    pthread_mutex_unlock(&(tm->work_mutex));

    return true;
}

