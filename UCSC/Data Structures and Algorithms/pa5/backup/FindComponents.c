//Nathaniel Basara
//nbasara@ucsc.edu
//pa5
//
//
//
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#include"List.h"
#include"Graph.h"


int main(int argc, char* argv[]){
  Graph G = NULL;
  Graph T = NULL;
  List S  = newList();
  FILE *in, *out;
  
  int n, s, d, holder;
  
  if( argc != 3 ){
      printf("Usage: %s <input file> <output file>\n", argv[0]);
      exit(1);
   }
  
   in = fopen(argv[1], "r");
   out = fopen(argv[2], "w");
   if( in==NULL ){
      printf("Unable to open file %s for reading\n", argv[1]);
      exit(1);
   }
   if( out==NULL ){
      printf("Unable to open file %s for writing\n", argv[2]);
      exit(1);
   }
  
  fscanf(in, "%d", &n);
  G = newGraph(n);
  for(int i = 1; i < n+1; i++){
    append(S, i);
  }
  
  fscanf(in, "%d", &s);
  fscanf(in, "%d", &d);
  while(s != 0 && d != 0){
    addArc(G, s, d);
    fscanf(in, "%d", &s);
    fscanf(in, "%d", &d);
  }
  fprintf(out, "Adjacency list representation of G:\n");
  printGraph(out, G);
  
  DFS(G, S);
  T = transpose(G);
  DFS(T, S);
  
  n = 0;
  for(int i = 1; i < getOrder(T)+1; i++){
    if(getParent(T, i) == NIL){
      n++;
    }
  }
  
  fprintf(out, "G contains %d strongly connected components:\n", n);
  
  s = 1;
  moveBack(S);
  while(s < n+1){
    while(getParent(T, get(S)) != NIL){
      movePrev(S);
    }
    holder = get(S);
    fprintf(out, "Component %d:", s);
    fprintf(out, " %d", get(S));
    moveNext(S);
    while(get(S) != -1){
      if(getParent(T, get(S)) == NIL){
        break;
      }
      fprintf(out, " %d", get(S));
      moveNext(S);
    }
    fprintf(out, "\n");
    moveBack(S);
    while (get(S) != holder){
      movePrev(S);
    }
    movePrev(S);
    s++;
  } 
  
  freeList(&S);
  freeGraph(&G);
  freeGraph(&T);
  
  fclose(in);
  fclose(out);

  return(0);
  
}