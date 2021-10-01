CC=gcc
CFLAGS=-g3
LDFLAGS=-pthread

.PHONY: clean all

all: mini_project

mini_project.o: mini_project.c
	$(CC) $(CFLAGS) -c mini_project.c 

mini_project: mini_project.o 
	$(CC) $(LDFLAGS) mini_project.o -o mini_project

clean:
	rm -f *.o *~ mini_project