# CECS 550 Mini-project
## by Nathan Basara

Synchronization using pthreads and semaphores.

## Program Description

Write a C program using pthreads that creates a desired amount of threads to execute a loop.  The desired threads is given as a program parameter.  All threads will modify and display a shared value during and after the loop.

## Requirements

* Must validate command line parameter to make sure it is a number, not sequence of alphanumerics or assorted characters.

* Be capable of functioning with large amount of threads.

* Must compile using a make file.

* Run without errors.

* Provide sufficent comments in code to help understand code.

## How to run and compile

1. Be inside directy with makefile and miniproject.c

2. If you want syncrhonization add -DPTHREAD_SYNC to CDFLAGS

3. Type 'make' into console to produce binary

4. Type './mini_project num_threads' where num_threads is a positve integer such that the program creates to run the program.

5. Type 'make clean' to remove binary and .o files