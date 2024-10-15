
import java.util.Scanner;

public class Game {

    final private char[] lettersIndex = new char[] {'A','B','C','D','E','F','G','H'};
    final private char[] numberIndex = new char[] {'8','7','6','5','4','3','2','1'};

    public Square[][] matrix = new Square[8][8];

    public Game() {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (i == 1) matrix[i][j] = new Pawn('B', i, j, true, false);
                else if (i == 6) matrix[i][j] = new Pawn('W', i, j, true, false);
                else if ((i == 0 && j == 0) || (i == 0 && j == 7)) matrix[i][j] = new Rook('B', i, j);
                else if ((i == 7 && j == 0) || (i == 7 && j == 7)) matrix[i][j] = new Rook('W', i, j);
                else if ((i == 0 && j == 1) || (i == 0 && j == 6)) matrix[i][j] = new Knight('B', i, j);
                else if ((i == 7 && j == 1) || (i == 7 && j == 6)) matrix[i][j] = new Knight('W', i, j);
                else if ((i == 0 && j == 2) || (i == 0 && j == 5)) matrix[i][j] = new Bishop('B', i, j);
                else if ((i == 7 && j == 2) || (i == 7 && j == 5)) matrix[i][j] = new Bishop('W', i, j);
                else if (i == 0 && j == 3) matrix[i][j] = new Queen('B', i, j);
                else if (i == 7 && j == 3) matrix[i][j] = new Queen('W', i, j);
                else if (i == 0 && j == 4) matrix[i][j] = new King('B', i, j);
                else if (i == 7 && j == 4) matrix[i][j] = new King('W', i, j);
                else matrix[i][j] = new Void(i, j);
            }
        }
    }

    public void printGame() {
        System.out.println("\n  A  B  C D  E F  G  H");
        for (int i = 0; i < matrix.length; i++) {
            System.out.printf("%d ", 8-i);
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j]);
                System.out.print(' ');
            }
            System.out.println();
        }
    }

    private int letterId(char letter) {
        for (int i = 0; i < lettersIndex.length; i++) {
            if (lettersIndex[i] == letter) return i;
        }
        return -1;
    }

    private int numberId(char number) {
        for (int i = 0; i < numberIndex.length; i++) {
            if (numberIndex[i] == number) return i;
        }
        return -1;
    }

    private int[] id(char[] c) {
        return new int[] { numberId(c[1]), letterId(c[0]) };
    }

    public void completeTurn(char color) {
        while (true) {
            Scanner in = new Scanner(System.in);
            if (color == 'W') System.out.print("\nWHITE MOVEMENT: ");
            if (color == 'B') System.out.print("\nBLACK MOVEMENT: ");
            char[] line = in.nextLine().toUpperCase().strip().toCharArray();
            int[] select = id(new char[]{line[0], line[1]});
            int[] movement = id(new char[]{line[line.length - 2], line[line.length - 1]});

            int selectX = select[0];
            int selectY = select[1];
            int movementX = movement[0];
            int movementY = movement[1];

            if (selectX >= 0 && selectX <= 7 && selectY >= 0 && selectY <= 7) {
                if (movementX >= 0 && movementX <= 7 && movementY >= 0 && movementY <= 7) {

                    if (matrix[selectX][selectY] instanceof Piece) {
                        if (((Piece) matrix[selectX][selectY]).color == color) {

                            if (((Piece) matrix[selectX][selectY]).canMove(movementX, movementY, matrix)) {
                                ((Piece) matrix[selectX][selectY]).move(movementX, movementY, matrix);
                                break;
                            } else System.out.println("INSIRA UM MOVIMENTO VALIDO");

                        } else System.out.println("SELECIONE UMA PEÇA SUA");
                    } else System.out.println("SELECIONE UMA PEÇA");

                } else System.out.println("INSIRA UM MOVIMENTO VALIDO");
            } else System.out.println("SELECIONE UMA PEÇA");
        }
    }
}
