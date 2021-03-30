package Question;

import IO.*;

import java.util.ArrayList;

public class EssayQ extends Question {
    int maxLength;
    int numOfResp;

    public int getMaxLength(){
        return this.maxLength;
    }

    public int getNumOfResp(){
        return this.numOfResp;
    }

    public EssayQ(){
        this.maxLength = 1000;
    }

    public EssayQ(String string){
        this.questionString = string;
    }

    public EssayQ(String string, int ml, int nr){
        this.questionString = string;
        if(ml > 0) {
            this.maxLength = ml;
        }
        else{
            Output.printString("Invalid argument for maxLength passed to the constructor. Setting it to 1000");
            this.maxLength = 1000;
        }
        if(nr > 0){
            this.numOfResp = nr;
        }
        else{
            Output.printString("Invalid argument passed for maxLength to the constructor. Setting it to 100");
            this.numOfResp = 1;
        }
    }

    public void setMaxLength(int i){
        if(i > 0) {
            this.maxLength = i;
        }
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
    public void readResponse(){
        ArrayList<String> resp = new ArrayList<String>();
        for(int i = 0; i < this.numOfResp; i++){
            String input = Input.getInputString();
            resp.add(input);
        }
        this.response = new Response(resp);
    }

    @Override
    public void displayQuestion(){
        Output.printString(this.getQuestionString());
    }

    @Override
    public Response readCorrectResponse(){
        return new Response("Nothing. There is no correct answer.");
    }
}
