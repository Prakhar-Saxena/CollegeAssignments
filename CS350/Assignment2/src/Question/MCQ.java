package Question;

import IO.*;

import java.util.ArrayList;

public class MCQ extends Question {
    ArrayList<String> choices;

    public MCQ(){
        this.choices = new ArrayList<String>();
    }

    public MCQ(String string, ArrayList<String> c){
        this.choices = c;
        this.questionString = string;
    }

    @Override
    public void displayQuestion() {
        Output.printString(this.questionString);
        Output.printChoicesArrayList(choices);
    }

    public void setChoices(ArrayList<String> c){
        this.choices = c;
    }

    public void addChoice(String c){
        this.choices.add(c);
    }
}
