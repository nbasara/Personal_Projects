//Nathaniel Basara
//nbasara@ucsc.edu
//pa1
//
//
//
import java.io.*;
import java.util.Scanner;
public class Lex {
	   public static void main(String[] args) throws IOException{
		      Scanner in = null;
		      PrintWriter out = null;
		      String line = null;
		      List A = new List();
		      int a, i = 1;
		      int counter =0;

		      if(args.length < 2){
		         System.err.println("Usage: stderr");
		         System.exit(1);
		      }
	      
		      // Open Scanner and Writer
		      in = new Scanner(new File(args[0]));
		      out = new PrintWriter(new FileWriter(args[1]));
		      

		      while( in.hasNextLine() ){
		         counter++;   //counting the number of lines
		         in.nextLine();
		      }
		      in = new Scanner(new File(args[0]));
		      
		      //Establishing Arrays of Strings and String Holders
		      String[] myArray = new String[counter+1];
		      String[] Holder = null;
		      String s1 = null;
		      String s2 = null;
		      //whatever the first element in doc will be first comparison
		      a = 1;
		      int n = 0;
		      A.moveFront();
		      while(in.hasNextLine()) {
		    	  line = in.nextLine()+" ";
		    	  Holder = line.split("\\s+");
		    	  n = Holder.length;
		    	  for(i=1; i<n; i++){
		              Holder[0] =Holder[0] + " " +Holder[i];
		           }
		    	  myArray[a] = Holder[0];
		    	  s1 = myArray[a];
		    	  s2 = myArray[1];
		    	  
		    	  if (A.empty()) {
		    		  A.append(a);
		    	  }
		    	  else if (s1.compareTo(s2)<0) {
		    		  while (s1.compareTo(s2)<0) {
		    			  A.movePrev();
		    			  if(A.cur == null) {
		    				  A.moveFront();
		    				  A.insertBefore(a);
		    				  break;
		    			  }
		    			  s2 =myArray[A.get()];
		    		  }
		    		  if(A.front() == a) {
		    			  i++;
		    		  }
		    		  else {
		    			  A.insertAfter(a);
		    		  }
		    	  }
		    	  else {
		    		  while (s1.compareTo(s2)>0) {
		    			  A.moveNext(); 
		    			  if(A.cur == null) {
		    				  A.moveBack();
		    				  A.insertAfter(a);
		    			  }
		    			  s2 =myArray[A.get()];
		    		  }
		    		  if(A.back() == a) {
		    			  i++;
		    		  }
		    		  else {
		    			  A.insertBefore(a);
		    		  }
		    	  }
		    	  A.moveFront();
		    	  while(1 !=A.get()) {
		    		  A.moveNext();
		    	  } 
		    	  
		    	  a++;
		      }
		      
		      A.moveFront();
		      for(a =1;a<counter+1;a++) {
		    	  out.println(myArray[A.get()]);
		    	  A.moveNext();
		      }
		     
		      in.close();
		      out.close();
		      
		   }
}