//-----------------------------------------------------------------------------
// FileIO.c
// Illustrates file input-output commands and text processing using the
// string functions strtok and strcat.
//-----------------------------------------------------------------------------

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "List.h"

#define MAX_LEN 160

int main(int argc, char * argv[]){
   List A = newList();
   int n, i, l, count=0;
   FILE *in, *out;
   char line[100];
   char tokenlist[1000];
  
   

   // check command line for correct number of arguments
   if( argc != 3 ){
      printf("Usage: %s <input file> <output file>\n", argv[0]);
      exit(1);
   }

   // open files for reading and writing 
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
 
  while( fgets(tokenlist, 100000, in) != NULL){
    count++;
  }
  printf("%d \n", count);
   
  char theArray[count][10000];
  in = fopen(argv[1], "r");
  
   i = 0 ;
  
  while( i < count){
    printf("%d \n", i);
    n = 0;
    l = 1;
    
    while( (line[n] = fgetc(in)) != '\n'  )  {
        theArray[i][n] = line[n];
        n++;
        }
    
    theArray[i][n] = '\0';
    line[n] = '\0';
    
    
    n = 0;
    
    
    if(theArray[get(A)][n] == line[n]){
          while(theArray[get(A)][n] == line[n]){
            if (theArray[get(A)][n] == '\0'){
              insertAfter(A,i);
              l = 0;
              break;
            }
            else if(line[n] == '\0'){
              insertBefore(A,i);
              l = 0;
              break;
            }
            else{
              n++;
          }
        }
      }
    
    
    
    if(isEmpty(A)){
      append(A, i);
    }
   
    else if(theArray[get(A)][n] > line[n]){
      prepend(A,i);
     }
    else if(get(A) == back(A)){
      append(A,i);
     }
    else{ 
      while((theArray[get(A)][n] < line[n]) || (l == 0)){
        if(get(A) == back(A)){
          append(A,i);
        }
        else{
          moveNext(A);
          n = 0;
          if(theArray[get(A)][n] == line[n]){
            while(theArray[get(A)][n] == line[n]){
              if (theArray[get(A)][n] == '\0'){
                insertAfter(A,i);
                l = 0;
                break;
              }
              else if(line[n] == '\0'){
                insertBefore(A,i);
                l =0;
                break;
              }
              else{
                n++; 
            }
          } 
        }
      }
     }
      if((back(A) == i) || (l ==0)){
        i = i;
      }
      else{
        insertBefore(A,i);
      }
  }
    i++;
    
    moveFront(A);
  }
  
  
  moveFront(A);
  while(get(A) != -1){
    n = 0;
    while( theArray[get(A)][n] != '\0'){
      fprintf(out, "%c", theArray[get(A)][n]);
      n++;
    }
    fprintf(out, "\n");
    moveNext(A);
  }

   /* close files */
   fclose(in);
   fclose(out);
   freeList(&A);

   return(0);
}
