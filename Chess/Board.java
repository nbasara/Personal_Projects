public class Board {
	Square[][] squares; //8x8 grid that contains squares
	
	public Board(){
		this.cleanBoard();
	}

	public Square getSquare(int x, int y) {
		if (x < 0 || x > 7 || y < 0 || y > 7) {
			throw new RuntimeException("Not a valid square");
		}
		return squares[x][y];
	}

	public void cleanBoard() {
		//create white pieces
		for(int i=0; i < 8; i++){
			squares[1][i] = new Square(1, i, new Pawn(true));
		}
		squares[0][0] = new Square(0, 0, new Rook(true));
		squares[0][7] = new Square(0, 7, new Rook(true));
		squares[0][1] = new Square(0, 1, new Knight(true));
		squares[0][6] = new Square(0, 6, new Knight(true));
		squares[0][2] = new Square(0, 2, new Bishop(true));
		squares[0][5] = new Square(0, 5, new Bishop(true));
		squares[0][3] = new Square(0, 3, new King(true));
		squares[0][4] = new Square(0, 4, new Queen(true));
		//create black pieces
		for(int i=0; i < 8; i++){
			squares[6][i] = new Square(1, i, new Pawn(false));
		}
		squares[7][0] = new Square(7, 0, new Rook(false));
		squares[7][7] = new Square(7, 7, new Rook(false));
		squares[7][1] = new Square(7, 1, new Knight(false));
		squares[7][6] = new Square(7, 6, new Knight(false));
		squares[7][2] = new Square(7, 2, new Bishop(false));
		squares[7][5] = new Square(7, 5, new Bishop(false));
		squares[7][3] = new Square(7, 3, new King(false));
		squares[7][4] = new Square(7, 4, new Queen(false));

	}
}
