import java.util.Scanner;

public class Main {
    static Scanner entrada = new Scanner(System.in);

    static char[][] gameMatrix = new char[][] {{' ', ' ', 'A', ' ', ' ', ' ', 'B', ' ', ' ', ' ', 'C', ' '}, {'1', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '}, {' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'}, {'2', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '}, {' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'}, {'3', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '}};

    static boolean playing = true;

    public static void main(String[] args) {

        while (true) {
            printGame();

            int turnos = 0;
            while (playing) {
                play('X');
                printGame();
                verificarGameOver('X');
                if (!playing) {
                    System.out.println("JOGADOR 'X' GANHOU!");
                    break;
                }
                turnos++;

                if (turnos == 9) {
                    System.out.println("EMPATE");
                    break;
                }

                play('O');
                printGame();
                verificarGameOver('O');
                if (!playing) {
                    System.out.println("JOGADOR 'O' GANHOU!");
                    break;
                }
                turnos++;
            }

            System.out.print("Jogar outra partida? (S/N) ");
            String userInput = ((entrada.next()).toUpperCase()).strip();
            if (userInput.equals("N")) break;
            reset();
            playing = true;
        }
    }

    public static void printGame() {
        for (char[] matrix : gameMatrix) {
            for (int j = 0; j < gameMatrix[0].length; j++) {
                System.out.print(matrix[j]);
            }
            System.out.println();
        }
    }

    public static void play(char xo) {
        while (true) {
            System.out.printf("Sua jogada [%s] ", xo);
            char[] play = (((entrada.nextLine()).toUpperCase()).strip()).toCharArray();

            if (play.length == 2) {
            if ((play[0] == 'A' || play[0] == 'B' || play[0] == 'C') && (play[1] == '1' || play[1] == '2' || play[1] == '3')) {
                int[] actualPlay = new int[2];

                if (play[0] == 'A') actualPlay[0] = 2;
                if (play[0] == 'B') actualPlay[0] = 6;
                if (play[0] == 'C') actualPlay[0] = 10;

                if (play[1] == '1') actualPlay[1] = 1;
                if (play[1] == '2') actualPlay[1] = 3;
                if (play[1] == '3') actualPlay[1] = 5;

                if (gameMatrix[actualPlay[1]][actualPlay[0]] == ' ') {
                    gameMatrix[actualPlay[1]][actualPlay[0]] = xo;
                    return;
                }
            }
            }
            System.out.println("INSIRA UMA JOGADA VALIDA!");
        }
    }

    public static void verificarGameOver(char xo) {
        // [1][2] / [1][6] / [1][10]
        // [3][2] / [3][6] / [3][10]
        // [5][2] / [5][6] / [5][10]
        // 8 possible WIN CONDITION

        // horizontalmente (3)
        for (int j = 1; j <= 5; j = j + 2) {
            if (gameMatrix[j][2] == xo && gameMatrix[j][6] == xo && gameMatrix[j][10] == xo) {
                playing = false;
                return;
            }
        }

        // verticalmente (3)
        for (int k = 2; k <= 10; k = k + 4) {
            if (gameMatrix[1][k] == xo && gameMatrix[3][k] == xo && gameMatrix[5][k] == xo) {
                playing = false;
                return;
            }
        }

        // diagonalmente (2)
        if (gameMatrix[1][2] == xo && gameMatrix[3][6] == xo && gameMatrix[5][10] == xo) {
            playing = false;
            return;
        }
        if (gameMatrix[1][10] == xo && gameMatrix[3][6] == xo && gameMatrix[5][2] == xo) {
            playing = false;
            return;
        }
    }

    public static void reset() {
        for (int i = 1; i <= 5; i = i + 2) {
            gameMatrix[i][2] = ' ';
            gameMatrix[i][6] = ' ';
            gameMatrix[i][10] = ' ';
        }
    }
}
