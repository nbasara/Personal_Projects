//Nathaniel Basara
//nbasara@ucsc.edu
//pa5
//
//
//
#include<stdio.h>
#include<stdlib.h>
#include "List.h"

typedef struct NodeObj{
	int data;
	struct NodeObj* next;
	struct NodeObj* prev;
} NodeObj;

typedef NodeObj* Node;

typedef struct ListObj{
	Node front;
	Node back;
	Node cur;
	int listLength;
	int index;
} ListObj;

Node newNode(int data){
  Node N = malloc(sizeof(NodeObj));
  N->data = data;
  N->next = NULL;
  N->prev = NULL;
  return (N);
}

void freeNode(Node* pN){
  if(pN != NULL && *pN!=NULL){
    free(*pN);
    *pN = NULL;
  }
}

List newList(void){
	List L;
	L = malloc(sizeof(ListObj));
	L->front = L->back = NULL;
	L->listLength = 0;
  L->index = -1;
  return(L);
}

void freeList(List* pL){
	if (pL != NULL && *pL != NULL){
    clear(*pL);
		free(*pL);
		*pL = NULL;
  }
}


int isEmpty(List L){
   if (L == NULL){
   printf("List ERROR: List DNE! NULL List\n");
    exit(1);
  }
  return (L->listLength == 0);
}

int length(List L){
	return L->listLength;
}

int index(List L){
	return L->index;
}

int front(List L){
	if (length(L) == 0){
		return -1;
	}
	return (L->front->data);
}

int back(List L){
	if (length(L) == 0){
		return -1;
	}
	return L->back->data;
}

int get(List L){
	if (L == NULL ){
   printf("List ERROR: List DNE! NULL List\n");
    exit(1);
  }
  if(L->cur == NULL){
    return -1;
  }
  else{
    return L->cur->data;
  }
}
           
           
int equals (List A, List B){
  if (A == NULL || B == NULL){
   printf("List ERROR: List DNE! NULL List\n");
    exit(1);
  }
	if(length(A) != length(B)){
		return 0;
	}
  moveFront(A);
  moveFront(B);
  while(get(A) != -1){
    if (get(A) != get(B)){
      return(0);
    }
    moveNext(A);
    moveNext(B);
  }
  return 1;
}

           
void clear(List L){
  while (!isEmpty(L)){
    moveFront(L);
		deleteFront(L);
	}
}

void moveFront(List L){
  if (length(L) == 0){
    L->cur = NULL;
    L->index = -1;
  }
  L->cur = L->front;
  L->index = 0;
}      

void moveBack(List L){
  if (length(L) == 0){
    L->cur = NULL;
    L->index = -1;
  }
  L->cur = L->back;
  L->index = length(L) - 1;
} 

void movePrev(List L){
  if (L->cur->prev == NULL){
    L->cur = NULL;
    L->index = -1;
  }
  else{
    L->index--;
    L->cur = L->cur->prev;
  }
} 

void moveNext(List L){
  if (L->cur->next == NULL){
    L->cur = NULL;
    L->index = -1;
  }
  else{
    L->index++;
    L->cur = L->cur->next;
  }
} 

void prepend(List L, int data){
  Node N = newNode(data);
  
  if (L == NULL){
   printf("List ERROR: List DNE! NULL List\n");
    exit(1);
  }
  if(isEmpty(L)){
    L->front = L->back = N;
  }
  else{
    N->next = L->front;
    L->front->prev = N;
    L->front = N;
  }
  if(index(L) != -1){
    L->index++;
  }
  L->listLength++;
}

void append(List L, int data){
  Node N = newNode(data);
  
  if (L == NULL){
   printf("List ERROR: List DNE! NULL List\n");
    exit(1);
  }
  if(isEmpty(L)){
    L->front = L->back = L->cur = N;
    L->index = 0;
  }
  else{
    N->prev = L->back;
    L->back->next = N;
    L->back = N;
  }
  L->listLength++;
}

void insertBefore(List L, int data){
  if (L == NULL){
   printf("List ERROR: List DNE! NULL List\n");
    exit(1);
  }
  if(isEmpty(L)){
    L->cur = NULL;
  }
  else if(index(L) == -1){
    L->index = -1;
  }
  else if (index(L) == 0){
    Node N = newNode(data);
    N->next = L->front;
    L->front->prev = N;
    L->front = N;
    L->index = L->index +1;
    L->listLength++;
  }
  else{
    Node N = newNode(data);
    N->prev = L->cur->prev;
    L->cur->prev->next = N;
    L->cur->prev = N;
    N->next = L->cur;
    L->index = L->index +1;
    L->listLength++;
  }
}

void insertAfter(List L, int data){
  if (L == NULL){
   printf("List ERROR: List DNE! NULL List\n");
    exit(1);
  }
  if(isEmpty(L)){
    L->cur = NULL;
  }
  else if(get(L) == -1){
    L->index = -1;
  }
  else if (index(L) == (length(L)-1)){
    Node N = newNode(data);
    N->prev = L->back;
    L->back->next = N;
    L->back = N;
    L->listLength++;
  }
  else{
    Node N = newNode(data);
    N->prev = L->cur;
    N->next = L->cur->next;
    L->cur->next->prev = N;
    L->cur->next = N;
    L->listLength++;
  }
}

void deleteFront(List L){
  Node N = NULL;
  if (L == NULL || isEmpty(L)){
   printf("List ERROR: List DNE! NULL List\n");
    exit(1);
  }
  if (index(L) == 0){
    L->cur = NULL;
    L->index = -1;
  }
  if(index(L) != -1){
    L->index--;
  }
  N = L->front;
  if (length(L) == 1){
    L->front = L->back = NULL;
  }
  else{
    L->front = L->front->next;
    L->front->prev = NULL;
  }
  L->listLength--;
  freeNode(&N);
}

void deleteBack(List L){
  Node N = NULL;
  if (L == NULL || isEmpty(L)){
   printf("List ERROR: List DNE! NULL List\n");
    exit(1);
  }
  if (index(L) == (L->listLength-1)){
    L->cur = NULL;
    L->index = -1;
  }
  N = L->back;
  if (length(L) == 1){
    L->front = L->back = NULL;
  }
  else{
    L->back = L->back->prev;
    L->back->next = NULL;
  }
  L->listLength--;
  freeNode(&N);
}

void delete(List L){
  if (L == NULL || isEmpty(L)){
   printf("List ERROR: List DNE! NULL List\n");
   exit(1);
  }
  else if(index(L) == 0){
    deleteFront(L);
  }
  else if(get(L) == back(L)){
    deleteBack(L);
  }
  else{
    L->cur->prev->next = L->cur->next;
    L->cur->next->prev = L->cur->prev;
    L->listLength--;
  }
  L->cur =  NULL;
  L->index = -1;
}


void printList(FILE* out, List L){
  Node temp = NULL;
  if (L == NULL){
   printf("List ERROR: List DNE! NULL List\n");
    exit(1);
  }
  for(temp = L->front; temp != NULL; temp = temp->next){
    fprintf(out, "%d ", temp->data);
  }
  freeNode(&temp);
}

List copyList(List L){
 List A = newList();
 moveFront(L);
 while(L->cur != NULL){
    append(A, L->cur->data);
    moveNext(L);
  }
  moveFront(L);
  return (A);
}

    









