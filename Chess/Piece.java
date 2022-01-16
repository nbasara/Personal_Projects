public abstract class Piece {
	// white = true; black = false
	private boolean active;
	private boolean color;

	public Piece(boolean color){
		this.setActive();
		this.setColor(color);
	}

	public void setActive() {
		this.active = true;
	}
	
	public void setDeactive() {
		this.active = false;
	}
	
	public boolean isActive() {
		return this.active;
	}

	public void  setColor(boolean col) {
		this.color = col;
	}

	public boolean isColor() {
		return this.color;
	}
}
