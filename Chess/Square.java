public class Square {
	private Piece piece;
	private int x;
	private int y;

	public Square(int x, int y, Piece piece) {
		this.setX(x);
		this.setY(y);
		this.setPiece(piece);
	}

	public void setPiece(Piece piece) {
		this.piece = piece;
	}

	public Piece getPiece() {
		return this.piece;
	}

	public void setX(int pos) {
		this.x = pos;
	}

	public int getX() {
		return this.x;
	}

	public void setY(int pos) {
		this.y = pos;
	}

	public int getY() {
		return this.Y;
	}
}
