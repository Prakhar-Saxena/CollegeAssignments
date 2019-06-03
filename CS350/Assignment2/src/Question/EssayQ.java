package Question;

import IO.*;

public class EssayQ extends Question {
    int maxLength;
    int numOfResp;

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
            Output.printError("Invalid argument for maxLength passed to the constructor. Setting it to 1000");
            this.maxLength = 1000;
        }
        if(nr > 0){
            this.numOfResp = ml;
        }
        else{
            Output.printError("Invalid argument passed for maxLength to the constructor. Setting it to 100");
            this.numOfResp = 1;
        }
    }

    public void setMaxLength(int i){
        if(i > 0) {
            this.maxLength = i;
        }
    }

    @Override
    public void displayQuestion(){
        Output.printString(this.questionString);
    }
}
