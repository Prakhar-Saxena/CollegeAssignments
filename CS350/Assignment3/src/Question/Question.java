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

    public void displayQuestionWithResponse(){
        this.displayQuestion();
        this.response.displayResponse();
    }

    public void displayQuestionString(){
        Output.printString(this.questionString);
    }

    public void modifyQuestionString(String string){
        this.questionString = string;
    }

    public String getQuestionString(){
        return this.questionString;
    }

    protected void setResponse(Response response){
        this.response = response;
    }

    public abstract void modifyQuestion();

    public abstract void readResponse();

    public void displayResponse(){
        this.response.displayResponse();
    }

    public Response getResponse(){
        return this.response;
    }

    public abstract Response readCorrectResponse();

//    public static void displayCorrectResponse(){}
}
