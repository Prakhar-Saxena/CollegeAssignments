package IO;

import Question.Question;

import javax.swing.*;
import java.util.ArrayList;

public class Output {
    public static void printNumArrayList(ArrayList<Integer> x){
        for(int i : x){
            System.out.println(i);
        }
    }

    public static void printNumArray(int[] x){
        for(int i : x){
            System.out.println(i);
        }
    }

    public static void printStringArrayList(ArrayList<String> x){
        for(String i : x){
            System.out.println(i);
        }
    }

    public static void printStringArrayListNumbered(ArrayList<String> x){
        for(int i = 0; i < x.size(); i ++){
            System.out.println((i+1)+") "+x.get(i));
        }
    }

    public static void printQuestionArrayList(ArrayList<Question> x){
        for(int i = 0; i < x.size(); i++){
            System.out.print((i+1)+") ");
            x.get(i).displayQuestion();
        }
    }

    public static void prtintQuestionWithResponse(ArrayList<Question> x){
        for(int i = 0; i < x.size(); i++){
            System.out.print((i+1)+") ");
            x.get(i).displayQuestionWithResponse();
        }
    }

    public static void printChoicesArrayList(ArrayList<String> choices){
        String[] alphabets = new String[26];
        for(char i = 'A', j = 0; i <='Z'; i++, j++){
            alphabets[j] = ""+i;
        }
        System.out.print("   ");
        for(int i = 0; i < choices.size(); i++){
            System.out.print(alphabets[i]+") "+choices.get(i)+"   ");
        }
        System.out.println();
    }

    public static void printMatchingChoicesArrayLists(ArrayList<String> ll, ArrayList<String> rl){
        String[] alphabets = new String[26];
        for(char i = 'A', j = 0; i <='Z'; i++, j++){
            alphabets[j] = ""+i;
        }
        for(int i = 0; i < ll.size(); i++){
            System.out.println("   "+alphabets[i]+") "+ll.get(i)+"   "+(i+1)+") "+rl.get(i));
        }
        System.out.println();
    }

    public static void printStringArray(String[] x){
        for(String i : x){
            System.out.println(i);
        }
    }

    public static void printQuestionCorrectAnswers(ArrayList<Question> questions, ArrayList<Response> responses){
        for(int i = 0; i < questions.size(); i++){
            System.out.print((i+1)+") ");
            questions.get(i).displayQuestion();
            responses.get(i);
        }
    }

    public static void printString(String string){
        System.out.println(string);
    }

    public static void printStringNoLine(String string){
        System.out.print(string);
    }

//    public static void printError(String errorString){
//        System.out.println(errorString);
//        JOptionPane.showMessageDialog(null, errorString, "Error", JOptionPane.INFORMATION_MESSAGE);
//    }
}
