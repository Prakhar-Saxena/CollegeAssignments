package Question;

import IO.Output;

import java.util.ArrayList;

public class RankingQ extends MatchingQ{
    public RankingQ(){
        this.leftList = new ArrayList<String>();
        this.rightList = new ArrayList<String>();
    }

    public RankingQ(String string){
        this.leftList = new ArrayList<String>();
        this.rightList = new ArrayList<String>();
        this.questionString = string;
    }

    public RankingQ(String string, ArrayList<String> ll){
        this.leftList = ll;
        for(int i = 1; i <= ll.size(); i++){
            this.rightList.add(Integer.toString(i));
        }
        this.questionString = string;
    }

    @Override
    public void displayQuestion(){
        Output.printString(this.questionString);
        Output.printChoicesArrayList(this.leftList);
    }
}
