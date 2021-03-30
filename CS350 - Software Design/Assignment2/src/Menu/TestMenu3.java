package Menu;

import SurveyTest.*;

public class TestMenu3 extends Menu1{
    protected Test testInMemory;

    public TestMenu3(){
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

    public TestMenu3(Test test){
        this.options = new String[7];
        this.options[0] = "Add a new T/F question";
        this.options[1] = "Add a new multiple choice question";
        this.options[2] = "Add a new short answer question";
        this.options[3] = "Add a new essay question";
        this.options[4] = "Add a new ranking question";
        this.options[5] = "Add a new matching question";
        this.options[6] = "Quit";
        this.numOfOptions = 7;
        this.testInMemory = test;
    }

    public Test returnTest(){
        executeMenu();
        return this.testInMemory;
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
        this.testInMemory.addTFQ();
    }

    public void addMCQ(){
        this.testInMemory.addMCQ();
    }

    public void addShortAnswerQ(){
        this.testInMemory.addShortAnswerQ();
    }

    public void addEssayQ(){
        this.testInMemory.addEssayQ();
    }

    public void addRankingQ(){
        this.testInMemory.addRankingQ();
    }

    public void addMatchingQ(){
        this.testInMemory.addMatchingQ();
    }
}
