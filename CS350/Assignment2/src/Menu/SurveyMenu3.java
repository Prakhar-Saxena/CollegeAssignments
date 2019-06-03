package Menu;

import IO.*;
import SurveyTest.*;

public class SurveyMenu3 extends Menu1 {
    protected Survey surveyInMemory;
    public SurveyMenu3(){
        this.options = new String[7];
        this.options[0] = "Add a new T/F question";
        this.options[1] = "Add a new multiple choice question";
        this.options[2] = "Add a new short answer question";
        this.options[3] = "Add a new essay question";
        this.options[4] = "Add a new ranking question";
        this.options[5] = "Add a new matching question";
        this.options[6] = "Quit";
        this.numOfOptions = 7;
    }

    public SurveyMenu3(Survey survey){
        this.options = new String[7];
        this.options[0] = "Add a new T/F question";
        this.options[1] = "Add a new multiple choice question";
        this.options[2] = "Add a new short answer question";
        this.options[3] = "Add a new essay question";
        this.options[4] = "Add a new ranking question";
        this.options[5] = "Add a new matching question";
        this.options[6] = "Quit";
        this.numOfOptions = 7;
        this.surveyInMemory = survey;
    }

    public Survey returnSurvey(){
        executeMenu();
        return this.surveyInMemory;
    }

    public void callFunctions(int x){
        switch (x){
            case 1:
                addTFQ();
                break;
            case 2:
                addMCQ();
                break;
            case 3:
                addShortAnswerQ();
                break;
            case 4:
                addEssayQ();
                break;
            case 5:
                addRankingQ();
                break;
            case 6:
                addMatchingQ();
                break;
            case 7:
                return;
        }
    }

    public void addTFQ(){
        this.surveyInMemory.addTFQ();
    }

    public void addMCQ(){
        this.surveyInMemory.addMCQ();
    }

    public void addShortAnswerQ(){
        this.surveyInMemory.addShortAnswerQ();
    }

    public void addEssayQ(){
        this.surveyInMemory.addEssayQ();
    }

    public void addRankingQ(){
        this.surveyInMemory.addRankingQ();
    }

    public void addMatchingQ(){
        this.surveyInMemory.addMatchingQ();
    }
}
