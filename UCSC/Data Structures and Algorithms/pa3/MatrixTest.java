//Nathaniel Basara
//nbasara@ucsc.edu
//pa3
//
//
//

public class MatrixTest {
	
	public static void main(String[] args){
		
		Matrix A = new Matrix(10);
    Matrix B = new Matrix(10);

		
		A.changeEntry(1,1,1.0);
    A.changeEntry(1,2,2.0);
    A.changeEntry(1,3,3.0);
    A.changeEntry(2,1,4.0);
    A.changeEntry(2,2,5.0);
    A.changeEntry(2,3,6.0);
    A.changeEntry(3,1,7.0);
    A.changeEntry(3,2,8.0);
    A.changeEntry(3,3,9.0);
    
    B.changeEntry(1,1,1.0);
    B.changeEntry(1,3,1.0);
    B.changeEntry(3,3,1.0);
    B.changeEntry(3,1,1.0);
    B.changeEntry(3,2,1.0);
    
    System.out.println(A);
		System.out.println(B);
    
    Matrix C = A.scalarMult(1.5);
   // System.out.println(C);
    C = A.add(B);
    System.out.println(C);
    C = A.add(A);
    System.out.println(C);
    C = B.sub(A);
    System.out.println(C);
    C = A.sub(A);
    System.out.println(C);
    C = A.transpose();
    System.out.println(C);
    C = A.mult(B);
    System.out.println(C);
    C = B.mult(B);
    System.out.println(C);
	}
}

// Output of this program:
// 1: (1, 1.0) (2, 2.0) (3, 3.0)
// 2: (1, 4.0) (2, 5.0) (3, 6.0)
// 3: (1, 7.0) (2, 8.0) (3, 9.0)
//
// 1: (1, 1.0) (3, 1.0)
// 3: (1, 1.0) (2, 1.0) (3, 1.0)
//
// 1: (1, 1.5) (2, 3.0) (3, 4.5)
// 2: (1, 6.0) (2, 7.5) (3, 9.0)
// 3: (1, 10.5) (2, 12.0) (3, 13.5)
//
// 1: (1, 2.0) (2, 2.0) (3, 4.0)
// 2: (1, 4.0) (2, 5.0) (3, 6.0)
// 3: (1, 8.0) (2, 9.0) (3, 10.0)
//
// 1: (1, 2.0) (2, 4.0) (3, 6.0)
// 2: (1, 8.0) (2, 10.0) (3, 12.0)
// 3: (1, 14.0) (2, 16.0) (3, 18.0)
//
// 1: (2, -2.0) (3, -2.0)
// 2: (1, -4.0) (2, -5.0) (3, -6.0)
// 3: (1, -6.0) (2, -7.0) (3, -8.0)
//
//1: (1, 1.0) (2, 4.0) (3, 7.0)
// 2: (1, 2.0) (2, 5.0) (3, 8.0)
// 3: (1, 3.0) (2, 6.0) (3, 9.0)
//
// 1: (1, 4.0) (2, 3.0) (3, 4.0)
// 2: (1, 10.0) (2, 6.0) (3, 10.0)
// 3: (1, 16.0) (2, 9.0) (3, 16.0)
//
// 1: (1, 2.0) (2, 1.0) (3, 2.0)
// 3: (1, 2.0) (2, 1.0) (3, 2.0)