package IO;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Input {
    public static int getInputInteger() throws InputMismatchException {
        while(true) {
            try {
                Scanner in = new Scanner(System.in);
                int input = in.nextInt();
                return input;
            }
            catch (Exception e){
                Output.printString("Wrong. Enter Again");
            }
        }
    }

    public static String getInputString() throws InputMismatchException{
        while(true) {
            try {
                Scanner in = new Scanner(System.in);
                String input = in.nextLine();
                return input;
            }
            catch (Exception e){
                Output.printString("Wrong. Enter Again");
            }
        }
    }
}
