package Question;

import IO.*;

import java.util.ArrayList;

public class ShortAnswerQ extends EssayQ{
    public ShortAnswerQ(){
        this.maxLength = 100;
    }

    public ShortAnswerQ(String string){
        this.questionString = string;
    }

    public ShortAnswerQ(String string, int ml, int nr){
        this.questionString = string;
        if(ml > 0 && ml <= 150) {
            this.maxLength = ml;
        }
        else{
            Output.printString("Invalid argument passed for maxLength to the constructor. Setting it to 100");
            this.maxLength = 150;
        }

        if(nr > 0){
            this.numOfResp = nr;
        }
        else{
            Output.printString("Invalid argument passed for maxLength to the constructor. Setting it to 100");
            this.numOfResp = 1;
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
        Output.printString(this.questionString);
    }

    @Override
    public Response readCorrectResponse(){
        ArrayList<String> resp = new ArrayList<String>();
        for(int i = 0; i < this.numOfResp; i++){
            String input = Input.getInputString();
            resp.add(input);
        }
        return new Response(resp);
    }
}
