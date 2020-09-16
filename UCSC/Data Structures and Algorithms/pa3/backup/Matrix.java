//Nathaniel Basara
//nbasara@ucsc.edu
//pa3
//
//
//


public class Matrix{

  int rows = 0; 
  int cols = 0; 
  int NNZ  = 0;
  
  //Creates an array of Lists
  List[] myMatrix;


  Matrix(int n){
    rows = n;
    NNZ = 0;
    myMatrix = new List[rows+1];
    int i = 1;
    while (i < (rows + 1) ) {
      List A = new List();
      myMatrix[i] = A;
      i++;
    }
  }


  void theMatrix() {
    myMatrix = new List[rows+1];
    int i = 1;
    while (i < (rows + 1) ) {
      List A = new List();
      myMatrix[i] = A;
      i++;
    }
  }

  static class Entry{
    int col;
    double value;

    Entry(int a, double b) {
      col = a;
      value = b;
      }
    
    public boolean equals(Object X){
      Entry N = (Entry) X;
      if (N.col == col && N.value == value){
        return true;
      }
      else{
        return false;
      }
    }
    
    
    
    public String toString() {
    	String Entries;
    	Entries = " (" + col + ", " + value + ") ";
    	return Entries;
    }
  }

  int getSize(){
    if(rows > 0){
      return rows;
    }
    else {
      return 0;
    }
  }

  int getNNZ(){
    return NNZ;
  }
  
  //Calls list equals
  public boolean equals(Object X){
    Matrix M = (Matrix) X;
    if(M.getNNZ() != getNNZ() ){
      return false;
    }
    if(M.getSize() != getSize()){
      return false;
    }
    for(int i = 1; i < getSize()+1; i++){
      if(!(myMatrix[i].equals(M.myMatrix[i]))){
        return false;
      }
    }
    return true;
  }

  
  // clears all lists and makes NNZ = 0
  void makeZero(){
    int row = 1;
    while ( row < (getSize() +1)){
      myMatrix[row].clear();
      row++;
    }
    NNZ = 0;
  }

  Matrix copy(){
      Matrix newMatrix = new Matrix(getSize());
      if (getNNZ() != 0) {

        int i = 1;
        while(i < (getSize()+ 1)) {
          myMatrix[i].moveFront();
          while(myMatrix[i].index() != -1) {
            Entry N = (Entry) myMatrix[i].get();
            newMatrix.changeEntry(i, N.col, N.value);
            myMatrix[i].moveNext();
          }
          i++;
        }
        newMatrix.NNZ = getNNZ();
      }
      return newMatrix;
    }
  
  void changeEntry(int i, int j, double x){
    Entry N = new Entry(j, x);
    int holder;
    int colHolder;
    holder = getNNZ();
    myMatrix[i].moveFront();
    while(holder == NNZ ) {
      if(myMatrix[i].length() == 0 || myMatrix[i].index() == -1 ) {
            colHolder = -1;
          }
    	else {
    		Entry t = (Entry) (myMatrix[i].get());
    	    colHolder = t.col;
    	}
      if(myMatrix[i].length() == 0) {
        if(x == 0) {
          holder++;
        }
        else {
          myMatrix[i].append(N);
          NNZ++;
        }
      }
      else if(colHolder > j) { 
        if(x == 0) {
          myMatrix[i].delete();
          NNZ--;
        }
        else {
          myMatrix[i].insertBefore(N);
          NNZ++;
        }
      }
      else if(colHolder == -1 ) {
        if(x == 0) {
          holder++;
        }
        else {
          myMatrix[i].append(N);
          NNZ++;
        }
      }
      else if(colHolder == j){
        if(x == 0) {
          myMatrix[i].delete();
          NNZ--;
        }
        else {
          myMatrix[i].insertBefore(N);
          myMatrix[i].delete();
          holder++;
        }
      }
      else {
        myMatrix[i].moveNext();
      }
    }
  }
  //multiplies by a given number
  Matrix scalarMult(double x){
    double holder;
    Matrix newMatrix = new Matrix(getSize());
    if(getNNZ() > 0) {
      for(int i = 1; i < (getSize()+1); i++) {
        myMatrix[i].moveFront();
        while(myMatrix[i].index() != -1) {
          Entry temp = (Entry) myMatrix[i].get();
          holder = temp.value*x;
          newMatrix.changeEntry(i, temp.col, holder);
          myMatrix[i].moveNext();
        }
      }
    }
    return newMatrix;
  }
  //adds and inserts if nonzero
  Matrix add(Matrix M){
    int c1Holder;
    double v1Holder;
    int c2Holder;
    double v2Holder;
    if(getSize() != M.getSize()) {
      throw new RuntimeException(
                "Matrix Error: add() called on non-eqaul Matrices");
    }
    else{
      double holder;
      Matrix newMatrix = new Matrix(getSize());
      if(equals(M)){
        newMatrix = scalarMult(2.0);
        return newMatrix;
      }
      for(int i = 1; i < (getSize()+1); i++) {
        myMatrix[i].moveFront();
        M.myMatrix[i].moveFront();
        while((myMatrix[i].index() != -1) || (M.myMatrix[i].index() != -1)) {
          if(myMatrix[i].index() != -1){
            Entry temp1 = (Entry) myMatrix[i].get();
            c1Holder = temp1.col;
            v1Holder = temp1.value;
          }
          else{
            Entry temp2 = (Entry) M.myMatrix[i].get();
            c1Holder = temp2.col+1;
            v1Holder = 0;
          }
          if(M.myMatrix[i].index() != -1){
            Entry temp2 = (Entry) M.myMatrix[i].get();
            c2Holder = temp2.col;
            v2Holder = temp2.value;
          }
          else{
            Entry temp1 = (Entry) myMatrix[i].get();
            c2Holder = temp1.col+1;
            v2Holder = 0;
          }
          if(c1Holder == c2Holder) {
            holder = v1Holder + v2Holder;
            newMatrix.changeEntry(i, c1Holder, holder);
            myMatrix[i].moveNext();
            M.myMatrix[i].moveNext();
          }
          else if(c1Holder > c2Holder) {
            newMatrix.changeEntry(i, c2Holder, v2Holder);
            M.myMatrix[i].moveNext();
          }
          else if(c1Holder < c2Holder) {
            newMatrix.changeEntry(i, c1Holder, v1Holder);
            myMatrix[i].moveNext();
          }
        }
      }
      return newMatrix;
    }
  }
  //Subtracts and Makes negative if nonzero entry
   Matrix sub(Matrix M){
    int c1Holder;
    double v1Holder;
    int c2Holder;
    double v2Holder;
    if(getSize() != M.getSize()) {
      throw new RuntimeException(
                "Matrix Error: add() called on non-eqaul Matrices");
    }
    else{
      double holder;
      Matrix newMatrix = new Matrix(getSize());
      if(equals(M)){
        newMatrix = scalarMult(0.0);
        return newMatrix;
      }
      for(int i = 1; i < (getSize()+1); i++) {
        myMatrix[i].moveFront();
        M.myMatrix[i].moveFront();
        while((myMatrix[i].index() != -1) || (M.myMatrix[i].index() != -1)) {
          if(myMatrix[i].index() != -1){
            Entry temp1 = (Entry) myMatrix[i].get();
            c1Holder = temp1.col;
            v1Holder = temp1.value;
          }
          else{
            Entry temp2 = (Entry) M.myMatrix[i].get();
            c1Holder = temp2.col+1;
            v1Holder = 0;
          }
          if(M.myMatrix[i].index() != -1){
            Entry temp2 = (Entry) M.myMatrix[i].get();
            c2Holder = temp2.col;
            v2Holder = temp2.value;
          }
          else{
            Entry temp1 = (Entry) myMatrix[i].get();
            c2Holder = temp1.col+1;
            v2Holder = 0;
          }
          if(c1Holder == c2Holder) {
            holder = v1Holder - v2Holder;
            newMatrix.changeEntry(i, c1Holder, holder);
            myMatrix[i].moveNext();
            M.myMatrix[i].moveNext();
          }
          else if(c1Holder > c2Holder) {
            v2Holder = -1*v2Holder;
            newMatrix.changeEntry(i, c2Holder, v2Holder);
            M.myMatrix[i].moveNext();
          }
          else if(c1Holder < c2Holder) {
            newMatrix.changeEntry(i, c1Holder, v1Holder);
            myMatrix[i].moveNext();
          }
        }
      }
      return newMatrix;
    }
  }
  
  //Creates a Transpose of a MATRIX only used in MULT
  Matrix transpose(){
    Matrix newMatrix = new Matrix(getSize());
    for(int i =1; i < (getSize()+1);i++){
      myMatrix[i].moveFront();
      while(myMatrix[i].index() != -1){
        Entry N  = (Entry) myMatrix[i].get();
        newMatrix.changeEntry(N.col, i, N.value);
        myMatrix[i].moveNext();
      }
    }
    return newMatrix;
  }
  
  //multiplies the contents of two lists
  private static double dot(List A, List B){
    A.moveFront();
    B.moveFront();
    double holder = 0;
    double total = 0;
    while(A.index() != -1 && B.index() != -1 ) {
        Entry temp1 = (Entry) A.get();
        Entry temp2 = (Entry) B.get();
        if(temp1.col == temp2.col) {
          holder = temp1.value * temp2.value;
          A.moveNext();
          B.moveNext();
        }
        else if(temp1.col > temp2.col || A.index == -1) {
          holder = 0;
          B.moveNext();
        }
        else if(temp1.col < temp2.col || B.index == -1) {
          holder = 0;
          A.moveNext();
        }
        total = total + holder;
      }
    return total;
  }
  
  //Uses dot and Transpose to simplfy process
  Matrix mult(Matrix M){
    Matrix newMatrix  = new Matrix(getSize());
    if(getSize() != M.getSize()) {
      throw new RuntimeException(
                "Matrix Error: add() called on non-eqaul Matrices");
    }
    else{
      Matrix temp = M.transpose();
      for (int i = 1; i<(getSize()+1);i++){
        for(int j = 1; j<(getSize()+1);j++){
          newMatrix.changeEntry(i,j,dot(myMatrix[i], temp.myMatrix[j]));
        }
      }
    }
    return newMatrix;
  }
  
  public String toString() {
		String temp1 = "";
    int  column;
    double val;
    if(getNNZ() == 0){
      return temp1;
    }
		for (int i= 1;i< (getSize()+1);i++) {
      if(myMatrix[i].length() > 0 ){
        temp1 = temp1+i+":";
        myMatrix[i].moveFront();
        while(myMatrix[i].index() != -1){
          Entry N = (Entry) myMatrix[i].get();
          column = N.col;
          val = N.value;
          temp1 = temp1 + N;
          myMatrix[i].moveNext();
        }
        temp1 = temp1 + "\n";
      }
		}
    return temp1;
	}
		  
  
}
