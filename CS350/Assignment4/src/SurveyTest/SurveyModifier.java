package SurveyTest;

import IO.*;

public class SurveyModifier {
    protected Survey targetSurvey;

    public SurveyModifier() {
        targetSurvey = new Survey();
    }

    public SurveyModifier(Survey survey){
        this.targetSurvey = survey;
    }

    public void ModifySurveyQuestions(){
        String isModifyQuestions = "Yes";
        while(isModifyQuestions.equalsIgnoreCase("Yes") || isModifyQuestions.equalsIgnoreCase("Y")){
            this.targetSurvey.displaySurvey();
            Output.printString("What question do you wish to modify? (Enter Number please)");
            int questionNumber = Input.getInputInteger();
            while(questionNumber<=0||questionNumber>this.targetSurvey.getNumberOfQuestions()){
                Output.printString("Invalid Input. Enter again.");
                questionNumber = Input.getInputInteger();
            }
            this.targetSurvey.modifyQuestion(questionNumber-1);
            Output.printString("Do you wish to modify any other questions?");
            isModifyQuestions = Input.getInputString();
        }
    }

}