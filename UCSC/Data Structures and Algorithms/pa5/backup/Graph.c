 //List.c
//Nathan Basara
//pa5
//
//
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "Graph.h"

#define UNDEF -2
#define NIL -3

#define WHITE -10
#define GRAY  -20
#define BLACK -30

typedef struct GraphObj{
  List* myGraph;
  int Order;    //number of vertices 
  int Size;     //number of edges 
  int* Color;   //stores color of vertex i
  int* Parent;  //u is the parent of v in BFS
  int* Disc;    //an array of ints that stores the discovery time
  int* Fin;
                
}GraphObj;


Graph newGraph(int n){
  Graph G;
  G = malloc(sizeof(GraphObj));
  G->Order = n;
  G->Size  = 0;
  G->myGraph = calloc(n+1, sizeof(List));
  G->Color = calloc(n+1, sizeof(int));
  G->Parent = calloc(n+1, sizeof(int));
  G->Disc = calloc(n+1, sizeof(int));
  G->Fin = calloc(n+1, sizeof(int));
  for(int i = 1; i < (n+1); i++){
    G->myGraph[i] = newList();
    G->Color[i] = WHITE;
    G->Parent[i]  = NIL;
    G->Disc[i]  = UNDEF;
    G->Fin[i] = UNDEF;
  }
  return G;
}

void freeGraph(Graph* pG){
  Graph temp = *pG;
  for(int i = 1; i < getOrder(temp) + 1; i++){
    freeList(&(temp->myGraph[i]));
  }
  free(temp->Color);
  free(temp->Parent);
  free(temp->Disc);
  free(temp->Fin);
  free(temp->myGraph);
  free(*pG);
  *pG = NULL;
}

/*** Access functions ***/
//returm number of vertices
int getOrder(Graph G){
  if(G == NULL){
    printf("Graph ERROR: Graph DNE! NULL Graph\n");
    exit(1);
  }
  return (G->Order);
}

//return the number of edges
int getSize(Graph G){
  if(G == NULL){
    printf("Graph ERROR: Graph DNE! NULL Graph\n");
    exit(1);
  }
  return (G->Size);
}

//return parent vertex of u
//return NIL if BFS() not called
//1<=u<=getOrder(G)
int getParent(Graph G, int u){
  if(G->Parent[u] == NIL){
    return NIL;
  }
  if(1 > u || u > getOrder(G)){
    printf("Graph ERROR: u is out of range!\n");
    exit(1);
  }
  return (G->Parent[u]);
}

//return time of discovery from most recent DFS
//return UNDEF if DFS not called
//1<=u<=getOrder(G)
int getDiscover(Graph G, int u){
  if(G->Disc[u] == UNDEF){
    return UNDEF;
  }
  if(1 > u || u > getOrder(G)){
    printf("Graph ERROR: u is out of range!\n");
    exit(1);
  }
  return G->Disc[u];
}

//
int getFinish(Graph G, int u){
   if(G->Fin[u] == UNDEF){
    return UNDEF;
  }
  if(1 > u || u > getOrder(G)){
    printf("Graph ERROR: u is out of range!\n");
    exit(1);
  }
  return G->Fin[u];
}

/*** Manipulation procedures ***/
//deletes all Edges in G
void makeNull(Graph G){
  for(int i = 1; i < (getOrder(G) + 1); i++){
    clear(G->myGraph[i]);
  }
  G->Size = 0;
}

//inserts new edge connecting u to v
//v gets added to u's adjancy list
//u gets added to v's adjancy list
//1<=u<=getOrder(G)
//1<=v<=getOrder(G)
void addEdge(Graph G, int u, int v){
  int a = getSize(G);
  if(1 > u || u > getOrder(G)){
    printf("Graph ERROR: u is out of range!\n");
    exit(1);
  }
  if(1 > v || v > getOrder(G)){
    printf("Graph ERROR: v is out of range!\n");
    exit(1);
  }
  if(isEmpty(G->myGraph[u])){
    append(G->myGraph[u], v);
  }
  else{
    moveFront(G->myGraph[u]);
    while(a == getSize(G)){
      if(index(G->myGraph[u]) == -1){
        append(G->myGraph[u], v);
        a++;
      }
      else if(get(G->myGraph[u]) > v){
        insertBefore(G->myGraph[u], v);
        a++;
      }
      else{
        moveNext(G->myGraph[u]);
      }
    }
  }
  a = getSize(G);
  if(isEmpty(G->myGraph[v])){
    append(G->myGraph[v], u);
  }
  else{
    moveFront(G->myGraph[v]);
    while(a == getSize(G)){
      if(index(G->myGraph[v]) == -1){
        append(G->myGraph[v], u);
        a++;
      }
      else if(get(G->myGraph[v]) > u){
        insertBefore(G->myGraph[v], u);
        a++;
      }
      else{
        moveNext(G->myGraph[v]);
      }
    } 
  }
  G->Size++;
}

//inserts new directed edge u to v
//v gets added to u's adjancy list
//but u does NOT get added to v's adjancy list
//1<=u<=getOrder(G)
//1<=v<=getOrder(G)
void addArc(Graph G, int u, int v){
  int a = getSize(G);
  if(1 > u || u > getOrder(G)){
    printf("Graph ERROR: u is out of range!  %d\n", u);
    exit(1);
  }
  if(1 > v || v > getOrder(G)){
    printf("Graph ERROR: v is out of range!  %d\n", v);
    exit(1);
  }
  if(isEmpty(G->myGraph[u])){
    append(G->myGraph[u], v);
    
  }
  else{
    moveFront(G->myGraph[u]);
    while(a == getSize(G)){
      if(index(G->myGraph[u]) == -1){
        append(G->myGraph[u], v);
        a++;
      }
      else if(get(G->myGraph[u]) > v){
        insertBefore(G->myGraph[u], v);
        a++;
      }
      else{
        moveNext(G->myGraph[u]);
      }
    }
  }
  G->Size++;
}

void Visit(Graph G, List S, int u, int *time){
    int v;
    *time = *time + 1;
    G->Disc[u] = *time;
    G->Color[u] = GRAY;
    if(!(isEmpty(G->myGraph[u]))){
     moveFront(G->myGraph[u]);
     while(index(G->myGraph[u]) != -1){
        v = get(G->myGraph[u]);
        if(G->Color[v] == WHITE){
          G->Parent[v] = u;
          Visit(G, S, v, time);
        }
        moveNext(G->myGraph[u]);
      }
    }
    G->Color[u] = BLACK;
    *time = *time + 1;
    G->Fin[u] = *time;
    prepend(S, u);
  }

void DFS(Graph G, List S){
  int time, u;
  if(length(S) != getOrder(G)){
    printf("List and Graph are not of same length!");
    exit(1);
  }
  moveFront(S);
  while(index(S) != -1){
    u = get(S);
    G->Color[u] =  WHITE;
    G->Parent[u] = NIL;
    moveNext(S);
  }
  time = 0;
  moveFront(S);
  while(index(S) != -1){
    u = get(S);
    if(G->Color[u] == WHITE){
      Visit(G, S, u, &time);
    }
    moveNext(S);
  }
  for(int i = 1;i < getOrder(G) +1;i++){
    deleteBack(S);
  }
}

/*** Other operations ***/

Graph transpose(Graph G){
  Graph N = newGraph(getOrder(G));
  if(G == NULL){
    return N;
  }
  else{
    for(int i = 1; i < getOrder(G)+1; i++){
      moveFront(G->myGraph[i]);
      while(get(G->myGraph[i]) != -1){
        addArc(N, get(G->myGraph[i]), i);
        moveNext(G->myGraph[i]);
      }
    }
  }
  return N;
} 

Graph copyGraph(Graph G){
   Graph N = newGraph(getOrder(G));
  if(G == NULL){
    return N;
  }
  else{
    N->Size = G->Size;
    for(int i = 1; i < getOrder(G)+1; i++){
      N->Disc[i] = G->Disc[i];
      N->Fin[i] = N->Fin[i];
      N->myGraph[i] = copyList(G->myGraph[i]);
    }
  }
  return N;
}

void printGraph(FILE* out, Graph G){
  for(int i = 1; i < getOrder(G) + 1;i++){
      fprintf(out, "%d: ", i);
      printList(out, G->myGraph[i]);
      fprintf(out, "\n");
    }
  fprintf(out, "\n");
  }

