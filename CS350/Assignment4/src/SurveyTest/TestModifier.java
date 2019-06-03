package SurveyTest;

import IO.Input;
import IO.Output;
import IO.Response;
import Question.EssayQ;

import java.util.ArrayList;

public class TestModifier {
    protected Test targetTest;

    public TestModifier() {
        targetTest = new Test();
    }

    public TestModifier(Test test){
        this.targetTest = test;
    }

    public void ModifyTestQuestions(){
        String isModifyQuestions = "Yes";
        while(isModifyQuestions.equalsIgnoreCase("Yes") || isModifyQuestions.equalsIgnoreCase("Y")){
            this.targetTest.displaySurvey();
            Output.printString("What question do you wish to modify? (Enter Number please)");
            int questionNumber = Input.getInputInteger();
            while(questionNumber<=0||questionNumber>this.targetTest.getNumberOfQuestions()){
                Output.printString("Invalid Input. Enter again.");
                questionNumber = Input.getInputInteger();
            }
            if (!(targetTest.getQuestion(questionNumber-1) instanceof EssayQ)){
                Output.printString("Do you wish to modify the correct Answer?");
                String isModifyCorrectAnswer = Input.getInputString();
                if(isModifyCorrectAnswer.equalsIgnoreCase("Yes") || isModifyCorrectAnswer.equalsIgnoreCase("Y")){
                    targetTest.modifyCorrectAnswer(questionNumber-1);
                }
                else{
                    Output.printString("No Correct Answers modified.");
                }
            }
            this.targetTest.modifyQuestion(questionNumber-1);
            Output.printString("Do you wish to modify any other questions?");
            isModifyQuestions = Input.getInputString();
        }
    }
}
