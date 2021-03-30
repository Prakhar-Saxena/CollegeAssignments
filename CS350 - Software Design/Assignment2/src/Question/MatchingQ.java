package Question;

import IO.Output;

import java.util.ArrayList;

public class MatchingQ extends Question{
    ArrayList<String> leftList;
    ArrayList<String> rightList;

    public MatchingQ(){
        this.leftList = new ArrayList<String>();
        this.rightList = new ArrayList<String>();
    }

    public MatchingQ(String string){
        this.leftList = new ArrayList<String>();
        this.rightList = new ArrayList<String>();
        this.questionString = string;
    }

    public MatchingQ(String string, ArrayList<String> ll, ArrayList<String> rl){
        this.leftList = ll;
        this.rightList = rl;
        this.questionString = string;
    }

    @Override
    public void displayQuestion(){
        Output.printString(this.questionString);
        Output.printMatchingChoicesArrayLists(this.leftList, this.rightList);
    }
}
