//List.c
//Nathan Basara
//pa3
//
//
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "Graph.h"

#define INF -2
#define NIL -3

#define WHITE -10
#define GRAY  -20
#define BLACK -30

typedef struct GraphObj{
  List* myGraph;
  int Order;    //number of vertices 
  int Size;     //number of edges
  int Source;   //source vertex 
  int* Color;   //stores color of vertex i
  int* Parent;  //u is the parent of v in BFS
  int* Dist;    //an array of ints that stores the distance from
                //most recent source
}GraphObj;


Graph newGraph(int n){
  Graph G;
  G = malloc(sizeof(GraphObj));
  G->Order = n;
  G->Size  = 0;
  G->Source = NIL;
  G->myGraph = calloc(n+1, sizeof(List));
  G->Color = calloc(n+1, sizeof(int));
  G->Parent = calloc(n+1, sizeof(int));
  G->Dist = calloc(n+1, sizeof(int));
  for(int i = 1; i < (n+1); i++){
    G->myGraph[i] = newList();
    G->Color[i] = WHITE;
    G->Parent[i]  = NIL;
    G->Dist[i]  = INF;
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
  free(temp->Dist);
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

//returns source vertex most recently used
//return NIL if BFS() not called
int getSource(Graph G){
  if(G->Source == NIL){
    return NIL;
  }
  return (G->Source);
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

//return distance from most recent BFS
//return INF if BFS not called
//1<=u<=getOrder(G)
int getDist(Graph G, int u){
  if(G->Dist[u] == INF){
    return INF;
  }
  if(1 > u || u > getOrder(G)){
    printf("Graph ERROR: u is out of range!\n");
    exit(1);
  }
  return G->Dist[u];
}

//appends to L the vertices of shortest path
//from source u.
//appends value NIL if path DNE
void getPath(List L, Graph G, int u){
  if(G->Color[u] != BLACK){
    append(L, NIL);
  }
  else if(u == G->Source){
    append(L, G->Source);
  }
  else{
    getPath(L, G, G->Parent[u]);
    append(L, u);
  }
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
    printf("Graph ERROR: u is out of range!\n");
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
    printf("Graph ERROR: u is out of range!\n");
    exit(1);
  }
  if(1 > v || v > getOrder(G)){
    printf("Graph ERROR: u is out of range!\n");
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

void BFS(Graph G, int s){
  G->Source = s;
  int u, v;
  for(int i = 1; i < (getOrder(G) + 1); i++){
    G->Color[i]  = WHITE;
    G->Dist[i]   = INF;
    G->Parent[i] = NIL;
  }
  G->Color[s]  = WHITE;
  G->Dist[s]   = 0;
  G->Parent[s] = NIL;
  if(isEmpty(G->myGraph[s])){
    return;
  }
  List Q = newList();
  prepend(Q, s);
  while(!isEmpty(Q)){
    moveFront(Q);
    u = front(Q);
    deleteFront(Q);
    moveFront(G->myGraph[u]);
    while(index(G->myGraph[u]) != -1){
      v = get(G->myGraph[u]);
      if(G->Color[v] == WHITE){
        G->Color[v] = GRAY;
        G->Dist[v] = G->Dist[u] + 1;
        G->Parent[v] = u;
        append(Q, v);
      }
      moveNext(G->myGraph[u]);
    }
    G->Color[u] = BLACK;
  }
  freeList(&Q);
}

/*** Other operations ***/
void printGraph(FILE* out, Graph G){
  for(int i = 1; i < getOrder(G) + 1;i++){
      fprintf(out, "%d: ", i);
      printList(out, G->myGraph[i]);
      fprintf(out, "\n");
    }
  fprintf(out, "\n");
  }

