package Question;

import IO.*;

import java.util.ArrayList;

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
    public void setChoices(ArrayList<String> c) { //setting choices not allowed
        Output.printError("Can't change choices for a True/False Question");
        return;
//        super.setChoices(c);
    }

    @Override
    public void addChoice(String c){ //setting choices not allowed
        Output.printError("Can't add more choices for a True/False Question");
        return;
    }
}
