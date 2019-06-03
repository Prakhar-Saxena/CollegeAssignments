package Question;

import IO.*;

import java.util.ArrayList;
import java.util.Arrays;

public class TrueFalseQ extends MCQ{
    public TrueFalseQ(){
        this.choices = new ArrayList<>();
        this.choices.add("True");
        this.choices.add("False");
    }

    public TrueFalseQ(String string){
        this.choices = new ArrayList<>();
        this.choices.add("True");
        this.choices.add("False");
        this.questionString = string;
    }

    @Override
    public void displayQuestion() {
        Output.printString(this.questionString);
        Output.printString("   "+"T/F");
    }

    @Override
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
    }

    @Override
    public void setChoices(ArrayList<String> c) { //setting choices not allowed
        Output.printString("Can't change choices for a True/False Question");
        return;
//        super.setChoices(c);
    }

    @Override
    public void addChoice(String c){ //setting choices not allowed
        Output.printString("Can't add more choices for a True/False Question");
        return;
    }

    @Override
    public void readResponse() {
        String input = Input.getInputString();
        this.response = new Response(input);
    }


}
