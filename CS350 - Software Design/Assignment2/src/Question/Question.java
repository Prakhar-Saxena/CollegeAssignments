package Question;
import java.io.Serializable;
import java.util.ArrayList;
import IO.*;
public abstract class Question implements Serializable {
    String questionString;
    Response response;

    public void displayQuestion(){
        Output.printString(this.questionString);
    }

    public void modifyQuestionString(String string){
        this.questionString = string;
    }

    public String getQuestionString(){
        return this.questionString;
    }

//    public static void displayCorrectResponse(){}
}
