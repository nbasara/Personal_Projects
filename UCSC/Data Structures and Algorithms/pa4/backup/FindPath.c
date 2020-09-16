#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#include"List.h"
#include"Graph.h"


int main(int argc, char* argv[]){
  Graph G =  NULL;
  List L = newList();
  FILE *in, *out;
  
  int n, s, d ;
  
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
  
  fscanf(in, "%d", &s);
  fscanf(in, "%d", &d);
  while(s != 0 && d != 0){
    addEdge(G, s, d);
    fscanf(in, "%d", &s);
    fscanf(in, "%d", &d);
  }
  printGraph(out, G);
  
  fscanf(in, "%d", &s);
  fscanf(in, "%d", &d);

  while(s != 0 && d != 0 ){
    BFS(G, s);
    if(getDist(G, d) == -2){
      fprintf(out, "The distance from %d to %d is infinity\n", s, d);
      fprintf(out, "No %d-%d path exists\n\n", s, d);
    }
    else{
      getPath(L, G, d);
      fprintf(out, "The distance from %d to %d is %d\n", s, d,  getDist(G, d));
      fprintf(out, "A shortest %d-%d path is: ",s, d);
      printList(out, L);
      clear(L);
      fprintf(out, "\n\n");
    }
    fscanf(in, "%d", &s);
    fscanf(in, "%d", &d);
  }

  
  freeList(&L);
  freeGraph(&G);
  
  fclose(in);
  fclose(out);

  return(0);
  
}