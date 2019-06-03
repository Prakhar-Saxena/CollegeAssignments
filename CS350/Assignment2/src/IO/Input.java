package IO;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Input {
    public static int getInputInteger() throws InputMismatchException {
        Scanner in = new Scanner(System.in);
        int input = in.nextInt();
        return input;
    }

    public static String getInputString() throws InputMismatchException{
        Scanner in = new Scanner(System.in);
        String input = in.nextLine();
        return input;
    }
}
