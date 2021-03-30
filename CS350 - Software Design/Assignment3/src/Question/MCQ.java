package Question;

import IO.*;

import javax.print.DocFlavor;
import java.util.ArrayList;
import java.util.Arrays;

public class MCQ extends Question {
    ArrayList<String> choices;

    public ArrayList<String> getChoices(){
        return this.choices;
    }

    public MCQ(){
        this.choices = new ArrayList<String>();
    }

    public MCQ(String string, ArrayList<String> c){
        this.choices = c;
        this.questionString = string;
    }

    @Override
    public void displayQuestion() {
        this.displayQuestionString();
        this.displayChoices();
    }

    public int getNumberOfChoices(){
        return this.choices.size();
    }

    public void displayChoices(){
        Output.printChoicesArrayList(choices);
    }

    protected void modifyChoice(int i, String string){
        if(i >= getNumberOfChoices()){
            return;
        }
        this.choices.set(i, string);
    }

    public void modifyQuestion(){
        Output.printString("Do You wish to modify the prompt?");
        String isModifyPrompt = Input.getInputString();
        if(!isModifyPrompt.equalsIgnoreCase("Yes") && !isModifyPrompt.equalsIgnoreCase("Y")){
            Output.printString("Not modifying the prompt");
        }
        else{
            this.displayQuestionString();
            Output.printString("Enter a new prompt");
            String newPrompt = Input.getInputString();
            this.modifyQuestionString(newPrompt);
            Output.printString("The prompt is probably modified.");
        }

        Output.printString("Do you wish to modify choices?");
        String isModifyChoices = Input.getInputString();

        if(!isModifyChoices.equalsIgnoreCase("Yes") && !isModifyChoices.equalsIgnoreCase("Y")){
            Output.printString("Not modifying the choices");
        }
        else {
            while (isModifyChoices.equalsIgnoreCase("Yes") || isModifyChoices.equalsIgnoreCase("Y")) {
                Output.printString("Which choice do you want to modify?");
                this.displayChoices();
                ArrayList<String> alphabets = new ArrayList<String>();
//            String[] alphabets = new String[this.getNumberOfChoices()];
                for (char i = 'A'; i < ('A' + this.getNumberOfChoices()); i++) {
                    alphabets.add("" + i);
                }
                String choiceSelected = Input.getInputString();
                while (!alphabets.contains(choiceSelected)) {
                    Output.printString("Invalid Input. Enter again.");
                    choiceSelected = Input.getInputString();
                }
                Output.printString("Enter the modified choice.");
                String modifedChoice = Input.getInputString();
                this.modifyChoice(alphabets.indexOf(choiceSelected), modifedChoice);
                Output.printString("Choice Modified");
                Output.printString("Do you wish to modify any more choices?");
                isModifyChoices = Input.getInputString();
            }
            Output.printString("Done modifying choices.");
        }
    }

    public void setChoices(ArrayList<String> c){
        this.choices = c;
    }

    public void addChoice(String c){
        this.choices.add(c);
    }

    @Override
    public void readResponse(){
        String input = Input.getInputString();
        this.response = new Response(input.toUpperCase());
    }

    @Override
    public Response readCorrectResponse(){
        String input = Input.getInputString();
        return new Response(input.toUpperCase());
    }
}
