
public class Rook extends Piece {
    public Rook(char color, int x, int y) {
        super(color, x, y);
    }

    @Override
    public void move(int moveX, int moveY, Square[][] gameMatrix) {
        gameMatrix[x][y] = new Void(x, y);
        gameMatrix[moveX][moveY] = new Rook(color, moveX, moveY);
    }

    @Override
    public boolean canMove(int moveX, int moveY, Square[][] gameMatrix) {
        return (availableMoves(gameMatrix))[moveX][moveY];
    }

    @Override
    public boolean[][] availableMoves(Square[][] gameMatrix) {
        boolean[][] gameMatrixBin = new boolean[8][8];

        for (int i = 0; i <= 7; i++) {
            for (int j = 0; j <= 7; j++) {
                gameMatrixBin[i][j] = false;

                gameMatrixBin[i][j] = verticalMove(i, j, gameMatrix);
                if (horizontalMove(i, j, gameMatrix)) gameMatrixBin[i][j] = true;
            }
        }

        return gameMatrixBin;
    }

    @Override
    public String toString() {
        if (color == 'W') return "♜";
        if (color == 'B') return "♖";
        else return "";
    }

    private boolean verticalMove(int moveX, int moveY, Square[][] gameMatrix) {
        if (moveY == y && moveX != x) {
            // localizando peças no caminho
            int upperBound = 0;
            int lowerBound = 7;

            for (int i = x-1; i >= 0; i--) { // UP
                if (gameMatrix[i][moveY] instanceof Piece) {
                    upperBound = i;
                    break;
                }
            }
            for (int i = x+1; i <= 7; i++) { // DOWN
                if (gameMatrix[i][moveY] instanceof Piece) {
                    lowerBound = i;
                    break;
                }
            }

            if (moveX <= lowerBound && moveX >= upperBound) {

                if (gameMatrix[moveX][moveY] instanceof Piece) {
                    return  ( ((Piece) gameMatrix[moveX][moveY]).color == target );
                } else return true;

            } else return false;
        } else return false;
    }

    private boolean horizontalMove(int moveX, int moveY, Square[][] gameMatrix) {
        if (moveX == x && moveY != y) {
            // localizando peças no caminho
            int leftBound = 0;
            int rightBound = 7;

            for (int i = y-1; i >= 0; i--) { // LEFT
                if (gameMatrix[moveX][i] instanceof Piece) {
                    leftBound = i+1;
                    break;
                }
            }
            for (int i = y+1; i <= 7; i++) { // RIGHT
                if (gameMatrix[moveX][i] instanceof Piece) {
                    rightBound = i-1;
                    break;
                }
            }

            if (moveY <= rightBound || moveY >= leftBound) {
                if (gameMatrix[moveX][moveY] instanceof Piece) {
                    return  ( ((Piece) gameMatrix[moveX][moveY]).color == target );
                } else return true;
            }
        }
        return false;
    }
}