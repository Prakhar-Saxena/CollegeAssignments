package Question;

import IO.*;

import java.util.ArrayList;
import java.util.Arrays;

public class MatchingQ extends Question{
    ArrayList<String> leftList;
    ArrayList<String> rightList;

    public ArrayList<String> getLeftList(){
        return this.leftList;
    }

    public ArrayList<String> getRightList(){
        return this.rightList;
    }

    public MatchingQ(){
        this.leftList = new ArrayList<String>();
        this.rightList = new ArrayList<String>();
    }

    public MatchingQ(String string){
        this.leftList = new ArrayList<String>();
        this.rightList = new ArrayList<String>();
        this.questionString = string;
    }

    public MatchingQ(String string, ArrayList<String> ll, ArrayList<String> rl){
        this.leftList = ll;
        this.rightList = rl;
        this.questionString = string;
    }

    public int getNumberOfChoices(){
        int leftListSize = this.leftList.size();
        int rightListSize = this.leftList.size();
        if (leftListSize == rightListSize){
            return leftListSize;
        }
        else{
            return 0;
        }
    }

    protected void modifyLeftChoice(int i, String string){
        if(i >= getNumberOfChoices()){
            return;
        }
        this.leftList.set(i, string);
    }

    protected void modifyRightChoice(int i, String string){
        if(i >= getNumberOfChoices()){
            return;
        }
        this.rightList.set(i, string);
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

        Output.printString("Do you wish to modify left hand side choices?");
        String isModifyLeftChoices = Input.getInputString();
        if(!isModifyLeftChoices.equalsIgnoreCase("Yes") && !isModifyLeftChoices.equalsIgnoreCase("Y")){
            Output.printString("Not modifying the left choices");
        }
        else {
            while (isModifyLeftChoices.equalsIgnoreCase("Yes") || isModifyLeftChoices.equalsIgnoreCase("Y")) {
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
                Output.printString("Do you wish to modify any more left hand side choices?");
                isModifyLeftChoices = Input.getInputString();
            }
        }
        Output.printString("Done modifying left hand side choices.");



        Output.printString("Do you wish to modify right hand side choices?");
        String isModifyRightChoices = Input.getInputString();

        if(!isModifyRightChoices.equalsIgnoreCase("Yes") && !isModifyRightChoices.equalsIgnoreCase("Y")){
            Output.printString("Not modifying the choices");
        }
        else {
            while (isModifyRightChoices.equalsIgnoreCase("Yes") || isModifyRightChoices.equalsIgnoreCase("Y")) {
                Output.printString("Which choice do you want to modify?");
                this.displayRightChoices();
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
                this.modifyRightChoice(alphabets.indexOf(choiceSelected), modifedChoice);
                Output.printString("Right Choice Modified");
                Output.printString("Do you wish to modify any more right hand side choices?");
                isModifyRightChoices = Input.getInputString();
            }
            Output.printString("Done modifying right hand side choices.");
        }
    }

    public void displayLeftChoices(){
        Output.printChoicesArrayList(this.leftList);
    }

    public void displayRightChoices(){
        Output.printChoicesArrayList(this.rightList);
    }

    public void displayChoices(){
        Output.printMatchingChoicesArrayLists(this.leftList, this.rightList);
    }

    @Override
    public void displayQuestion(){
        this.displayQuestionString();
        this.displayChoices();
    }

    @Override
    public void readResponse(){
        ArrayList<String> resp = new ArrayList<String>();
        for(int i = 0; i < this.getNumberOfChoices(); i++){
            String input = Input.getInputString();
            resp.add(input.toUpperCase());
        }
        this.response = new Response(resp);
    }

    @Override
    public Response readCorrectResponse(){
        ArrayList<String> resp = new ArrayList<String>();
        for(int i = 0; i < this.getNumberOfChoices(); i++){
            String input = Input.getInputString();
            resp.add(input.toUpperCase());
        }
        return new Response(resp);
    }
}
