
public class Bishop extends Piece {
    public Bishop(char color, int x, int y) {
        super(color, x, y);
    }

    @Override
    public void move(int moveX, int moveY, Square[][] gameMatrix) {
        gameMatrix[x][y] = new Void(x, y);
        gameMatrix[moveX][moveY] = new Bishop(color, moveX, moveY);
    }

    @Override
    public boolean canMove(int moveX, int moveY,Square[][] gameMatrix) {
        return (availableMoves(gameMatrix))[moveX][moveY];
    }

    @Override
    public boolean[][] availableMoves(Square[][] gameMatrix) {
        boolean[][] gameMatrixBin = new boolean[8][8];

        for (int i = 0; i <= 7; i++) {
            for (int j = 0; j <= 7; j++) {
                gameMatrixBin[i][j] = false;

                gameMatrixBin[i][j] = mainDiagonalMove(i, j, gameMatrix);
                if (secondaryDiagonalMove(i, j, gameMatrix)) gameMatrixBin[i][j] = true;
            }
        }

        return gameMatrixBin;
    }

    @Override
    public String toString() {
        if (color == 'W') return "♝";
        if (color == 'B') return "♗";
        else return "";
    }

    private boolean mainDiagonalMove(int moveX, int moveY, Square[][] gameMatrix) {
        // up
        for (int i = 1, j = 1; x - i >= 0 && y - j >= 0 ; i++, j++) { // - -
            // localizando peças no caminho
            if (gameMatrix[x-i][y-j] instanceof Piece) {
                // verificando movimento
                if (moveX == x-i && moveY == y-j) {
                    return ( ((Piece) gameMatrix[moveX][moveY]).color == target );
                } else break;
            }
            // verificando movimento

            if (moveX == x-i && moveY == y-j) {
                return true;
            }
        }

        // down
        for (int i = 1, j = 1; x + i <= 7 && y + j <= 7 ; i++, j++) { // + +
            // localizando peças no caminho
            if (gameMatrix[x+i][y+j] instanceof Piece) {
                // verificando movimento
                if (moveX == x+i && moveY == y+j) {
                    return ( ((Piece) gameMatrix[moveX][moveY]).color == target );
                } else break;
            }
            // verificando movimento
            if (moveX == x+i && moveY == y+j) {
                return true;
            }
        }

        return false;
    }

    private boolean secondaryDiagonalMove(int moveX, int moveY, Square[][] gameMatrix) {
        // up
        for (int i = 1, j = 1; x - i >= 0 && y + j <= 7 ; i++, j++) { // - +
            // localizando peças no caminho
            if (gameMatrix[x-i][y+j] instanceof Piece) {
                // verificando movimento
                if (moveX == x-i && moveY == y+j) {
                    return ( ((Piece) gameMatrix[moveX][moveY]).color == target );
                } else break;
            }
            // verificando movimento
            if (moveX == x-i && moveY == y+j) {
                return true;
            }
        }

        // down
        for (int i = 1, j = 1; x + i <= 7 && y - j >= 0 ; i++, j++) { // + -
            // localizando peças no caminho
            if (gameMatrix[x+i][y-j] instanceof Piece) {
                // verificando movimento
                if (moveX == x+i && moveY == y-j) {
                    return ( ((Piece) gameMatrix[moveX][moveY]).color == target );
                } else break;
            }
            // verificando movimento
            if (moveX == x+i && moveY == y-j) {
                return true;
            }
        }

        return false;
    }
}
