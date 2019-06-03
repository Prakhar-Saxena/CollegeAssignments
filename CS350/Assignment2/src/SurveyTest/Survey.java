package SurveyTest;

import IO.*;
import Question.*;

import java.io.IOException;
import java.io.ObjectStreamException;
import java.io.Serializable;
import java.util.ArrayList;

public class Survey implements Serializable {
    String name;
    protected ArrayList<Question> questions; // = new ArrayList<Question>();
    protected ArrayList<Response> responses; // = new ArrayList<Response>();

    public Survey(){
        this.questions = new ArrayList<Question>();
        this.responses = new ArrayList<Response>();
    }

    public Survey(String n){
        this.questions = new ArrayList<Question>();
        this.responses = new ArrayList<Response>();
        this.name = n;
    }

    public static Survey create(String name){
        return new Survey(name);
    }

    public void displaySurvey(){
        Output.printString("Survey: " + this.name);
        Output.printQuestionArrayList(this.questions);
        Output.printString("");
    }

    public void addTFQ(){
        Output.printString("Enter the prompt for your True/False Question:");
        String qPrompt = Input.getInputString();
        TrueFalseQ trueFalseQ = new TrueFalseQ(qPrompt);
        this.questions.add(trueFalseQ);
        Output.printString("True/False Question Added.\n");
    }

    public void addMCQ(){
        Output.printString("Enter the prompt for your Multiple-Choice Question:");
        String qPrompt =  Input.getInputString();
        Output.printString("Enter the number of choices for your Multiple-Choice Question:");
        int qNumberOfChoices = Input.getInputInteger();
        ArrayList<String> choices = new ArrayList<String>();
        for(int i = 1; i <= qNumberOfChoices; i++){
            Output.printString("Enter choice #"+i);
            String choice = Input.getInputString();
            choices.add(choice);
        }
        MCQ mcq = new MCQ(qPrompt, choices);
        this.questions.add(mcq);
        Output.printString("Multiple-Choice Question Added.\n");
    }

    public void addShortAnswerQ(){
        Output.printString("Enter the prompt for your Short Answer Question:");
        String qPrompt = Input.getInputString();
        Output.printString("Enter the size for your Short Answer Question (not over than 150):");
        int qSize = Input.getInputInteger();
        Output.printString("Enter the number of responses for your Short Answer Question:");
        int qNumOfResp = Input.getInputInteger();
        ShortAnswerQ shortAnswerQ = new ShortAnswerQ(qPrompt, qSize,qNumOfResp);
        this.questions.add(shortAnswerQ);
        Output.printString("Short-Answer Question Added.\n");
    }

    public void addEssayQ(){
        Output.printString("Enter the prompt for your Essay Question:");
        String qPrompt = Input.getInputString();
        Output.printString("Enter the size for your Essay Question:");
        int qSize = Input.getInputInteger();
        Output.printString("Enter the number of responses for your Essay Question:");
        int qNumOfResp = Input.getInputInteger();
        EssayQ essayQ = new EssayQ(qPrompt, qSize, qNumOfResp);
        this.questions.add(essayQ);
        Output.printString("Essay Question Added.\n");
    }

    public void addRankingQ(){
        Output.printString("Enter the prompt for your Ranking Question:");
        String qPrompt = Input.getInputString();
        Output.printString("Enter the number of items for your Ranking Question:");
        int qNumberOfItems = Input.getInputInteger();
        ArrayList<String> items = new ArrayList<String>();
        for(int i = 1; i <= qNumberOfItems; i++){
            Output.printString("Enter item #"+i);
            String item = Input.getInputString();
            items.add(item);
        }
        RankingQ rankingQ = new RankingQ(qPrompt, items);
        this.questions.add(rankingQ);
        Output.printString("Ranking Question Added.\n");
    }

    public void addMatchingQ(){
        Output.printString("Enter the prompt for your Matching Question:");
        String qPrompt = Input.getInputString();
        Output.printString("Enter the number of items for your Matching Question");
        int qNumberOfItems = Input.getInputInteger();
        ArrayList<String> ll = new ArrayList<String>();
        Output.printString("Enter items for your left hand side list:");
        for(int i = 1; i <= qNumberOfItems; i++){
            Output.printString("Enter item #"+i);
            String item = Input.getInputString();
            ll.add(item);
        }
        ArrayList<String> rl = new ArrayList<String>();
        Output.printString("Enter items for your right hand side list:");
        for(int i = 1; i <= qNumberOfItems; i++){
            Output.printString("Enter item #"+i);
            String item = Input.getInputString();
            rl.add(item);
        }
        MatchingQ matchingQ = new MatchingQ(qPrompt, ll, rl);
        this.questions.add(matchingQ);
        Output.printString("Matching Question Added.\n");
    }
//
//    private void writeObject(java.io.ObjectOutputStream out) throws IOException{
//
//    }
//
//    private void readObject(java.io.ObjectInputStream in) throws IOException, ClassNotFoundException{
//
//    }
//
//    private void readObjectNoData() throws ObjectStreamException{
//
//    }
}
