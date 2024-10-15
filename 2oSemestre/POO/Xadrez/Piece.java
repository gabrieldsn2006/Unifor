
import java.util.Scanner;

public abstract class Piece extends Square {
    protected char color;
    protected char target;

    public Piece(char color, int x, int y) {
        this.color = color;
        if (color == 'W') target = 'B';
        if (color == 'B') target = 'W';
        this.x = x;
        this.y = y;
    }

    public abstract void move(int moveX, int moveY, Square[][] gameMatrix);

    public abstract boolean canMove(int moveX, int moveY, Square[][] gameMatrix);

    public abstract boolean[][] availableMoves(Square[][] gameMatrix);

}