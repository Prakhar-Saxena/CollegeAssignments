package Question;

import IO.*;

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
            Output.printError("Invalid argument passed for maxLength to the constructor. Setting it to 100");
            this.maxLength = 150;
        }

        if(nr > 0){
            this.numOfResp = ml;
        }
        else{
            Output.printError("Invalid argument passed for maxLength to the constructor. Setting it to 100");
            this.numOfResp = 1;
        }
    }

    @Override
    public void displayQuestion(){
        Output.printString(this.questionString);
    }
}
