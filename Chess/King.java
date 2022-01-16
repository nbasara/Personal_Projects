public class King extends Piece {

    private boolean hasCastled = false;

    public King(boolean color) {
        super(color);
    }

    public boolean isCastleDone(){
        return this.hasCastled;
    }

    public void setCastle(){
        this.hasCastled = true;
    }

    public boolean isValidCastle(Board board, Square start, Square end) {

        if (this.hasCastled) {
            return false;
        }

        /*
        check whether the king has moved
        check whether the rook has moved
        will move to end position put the king in check 
         */
        return true;
}
