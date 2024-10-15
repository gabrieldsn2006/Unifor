
public class King extends Piece {
    public King(char color, int x, int y) {
        super(color, x, y);
    }

    @Override
    public void move(int moveX, int moveY, Square[][] gameMatrix) {
        gameMatrix[x][y] = new Void(x, y);
        gameMatrix[moveX][moveY] = new King(color, moveX, moveY);
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

                gameMatrixBin[i][j] = upMove(i, j, gameMatrix);
                if (upperRightMove(i, j, gameMatrix)) gameMatrixBin[i][j] = true;
                if (rightMove(i, j, gameMatrix)) gameMatrixBin[i][j] = true;
                if (lowerRightMove(i, j, gameMatrix)) gameMatrixBin[i][j] = true;
                if (downMove(i, j, gameMatrix)) gameMatrixBin[i][j] = true;
                if (lowerLeftMove(i, j, gameMatrix)) gameMatrixBin[i][j] = true;
                if (leftMove(i, j, gameMatrix)) gameMatrixBin[i][j] = true;
                if (upperLeftMove(i, j, gameMatrix)) gameMatrixBin[i][j] = true;
            }
        }

        return gameMatrixBin;
    }

    @Override
    public String toString() {
        if (color == 'W') return "♚";
        if (color == 'B') return "♔";
        else return "";
    }

    boolean upMove(int moveX, int moveY, Square[][] gameMatrix) {
        if (moveX == x-1 && moveY == y) {
            if (gameMatrix[moveX][moveY] instanceof Piece) {
                return ( ((Piece) gameMatrix[moveX][moveY]).color == target );
            } else return true;
        } else return false;
    }

    boolean upperRightMove(int moveX, int moveY, Square[][] gameMatrix) {
        if (moveX == x-1 && moveY == y+1) {
            if (gameMatrix[moveX][moveY] instanceof Piece) {
                return ( ((Piece) gameMatrix[moveX][moveY]).color == target );
            } else return true;
        } else return false;
    }

    boolean rightMove(int moveX, int moveY, Square[][] gameMatrix) {
        if (moveX == x && moveY == y+1) {
            if (gameMatrix[moveX][moveY] instanceof Piece) {
                return ( ((Piece) gameMatrix[moveX][moveY]).color == target );
            } else return true;
        } else return false;
    }

    boolean lowerRightMove(int moveX, int moveY, Square[][] gameMatrix) {
        if (moveX == x+1 && moveY == y+1) {
            if (gameMatrix[moveX][moveY] instanceof Piece) {
                return ( ((Piece) gameMatrix[moveX][moveY]).color == target );
            } else return true;
        } else return false;
    }

    boolean downMove(int moveX, int moveY, Square[][] gameMatrix) {
        if (moveX == x+1 && moveY == y) {
            if (gameMatrix[moveX][moveY] instanceof Piece) {
                return ( ((Piece) gameMatrix[moveX][moveY]).color == target );
            } else return true;
        } else return false;
    }

    boolean lowerLeftMove(int moveX, int moveY, Square[][] gameMatrix) {
        if (moveX == x+1 && moveY == y-1) {
            if (gameMatrix[moveX][moveY] instanceof Piece) {
                return ( ((Piece) gameMatrix[moveX][moveY]).color == target );
            } else return true;
        } else return false;
    }

    boolean leftMove(int moveX, int moveY, Square[][] gameMatrix) {
        if (moveX == x && moveY == y-1) {
            if (gameMatrix[moveX][moveY] instanceof Piece) {
                return ( ((Piece) gameMatrix[moveX][moveY]).color == target );
            } else return true;
        } else return false;
    }

    boolean upperLeftMove(int moveX, int moveY, Square[][] gameMatrix) {
        if (moveX == x-1 && moveY == y-1) {
            if (gameMatrix[moveX][moveY] instanceof Piece) {
                return ( ((Piece) gameMatrix[moveX][moveY]).color == target );
            } else return true;
        } else return false;
    }
}