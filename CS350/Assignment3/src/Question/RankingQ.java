package Question;

import IO.*;

import java.util.ArrayList;
import java.util.Arrays;

public class RankingQ extends MatchingQ{
    public RankingQ(){
        this.leftList = new ArrayList<String>();
        this.rightList = new ArrayList<String>();
    }

    public RankingQ(String string){
        this.leftList = new ArrayList<String>();
        this.rightList = new ArrayList<String>();
        this.questionString = string;
    }

    public RankingQ(String string, ArrayList<String> ll){
        this.leftList = ll;
        for(int i = 1; i <= ll.size(); i++){
            this.rightList.add(Integer.toString(i));
        }
        this.questionString = string;
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

        Output.printString("Do you wish to modify choices?");
        String isModifyChoices = Input.getInputString();
        if(!isModifyChoices.equalsIgnoreCase("Yes") && !isModifyChoices.equalsIgnoreCase("Y")){
            Output.printString("Not modifying the left choices");
        }
        else {
            while (isModifyChoices.equalsIgnoreCase("Yes") || isModifyChoices.equalsIgnoreCase("Y")) {
                Output.printString("Which choice do you want to modify?");
                this.displayLeftChoices();
                ArrayList<String> alphabets = new ArrayList<String>();
//            String[] alphabets = new String[this.getNumberOfChoices()];
                for (char i = 'A'; i <= ('A' + this.getNumberOfChoices()); i++) {
                    alphabets.add("" + i);
                }
                String choiceSelected = Input.getInputString();
                while (!alphabets.contains(choiceSelected)) {
                    Output.printString("Invalid Input. Enter again.");
                    choiceSelected = Input.getInputString();
                }
                Output.printString("Enter the modified choice.");
                String modifedChoice = Input.getInputString();
                this.modifyLeftChoice(alphabets.indexOf(choiceSelected), modifedChoice);
                Output.printString("Left Choice Modified");
                Output.printString("Do you wish to modify any more choices?");
                isModifyChoices = Input.getInputString();
            }
        }
        Output.printString("Done modifying choices.");
        this.rightList = new ArrayList<>();
        for(int i = 1; i <= this.leftList.size(); i++){
            this.rightList.add(Integer.toString(i));
        }
    }

    @Override
    public void displayQuestion(){
        Output.printString(this.questionString);
        Output.printChoicesArrayList(this.leftList);
    }
}
