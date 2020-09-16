//Nathaniel Basara
//nbasara@ucsc.edu
//pa3
//
//
//

import java.io.*;
import java.util.Scanner;

public class Sparse {
  public static void main(String[] args) throws IOException{
    Scanner in = null;
    PrintWriter out = null;
    String line = null;
    String[] Holder = null;

    double dub;
    int size = 0;
    int aNon = 0;
    int bNon = 0;
    int  row,  col;
    int counter = 0;
    int a;
    
    //Matrix C used as holder
    Matrix A = new Matrix(0);
    Matrix B = new Matrix(0);
    Matrix C = new Matrix(0);

    if(args.length < 2){
      System.err.println("Usage: stderr");
      System.exit(1);
    }

    // Open Scanner and Writer
    in = new Scanner(new File(args[0]));
    out = new PrintWriter(new FileWriter(args[1]));
    
    


    while( in.hasNextLine() ){
      counter++;                    //counting the number of lines
      line = in.nextLine()+" ";
      Holder = line.split("\\s+");
      a = Holder.length;
      
      //Reads first line
      if(counter == 1){
        size = Integer.parseInt(Holder[0]);
        aNon = Integer.parseInt(Holder[1]);
        bNon = Integer.parseInt(Holder[2]);
        A = new Matrix(size);
        B = new Matrix(size);
        C = new Matrix(size);
      }
      
      //Takes input for Matrix A
      else if(counter > 2 && counter < (3 + aNon)){
        row  = Integer.parseInt(Holder[0]);
        col  = Integer.parseInt(Holder[1]);
        dub  = Double.parseDouble(Holder[2]);
        A.changeEntry(row, col, dub);
      }
      
      //Takes inputs for Matrix B
      else if(counter > (aNon +3)){
        row  = Integer.parseInt(Holder[0]);
        col  = Integer.parseInt(Holder[1]);
        dub  = Double.parseDouble(Holder[2]);
        B.changeEntry(row, col, dub);
      }
    }
    
    //Performs all functions and outputs to file
    out.println("A has "+A.getNNZ()+" non-zero entries:");
    out.println(A);
    out.println("B has "+B.getNNZ()+" non-zero entries:");
    out.println(B);
    C = A.scalarMult(1.5);
    out.println("(1.5)*A =");
    out.println(C);
    C = A.add(B);
    out.println("A+B =");
    out.println(C);
    C = A.add(A);
    out.println("A+A =");
    out.println(C);
    C = B.sub(A);
    out.println("B-A =");
    out.println(C);
    C = A.sub(A);
    out.println("A-A =");
    out.println(C);
    C = A.transpose();
    out.println("Transpose(A) =");
    out.println(C);
    C = A.mult(B);
    out.println("A*B =");
    out.println(C);
    C = B.mult(B);
    out.println("B*B =");
    out.println(C);
    
    in.close();
    out.close();
    }
}