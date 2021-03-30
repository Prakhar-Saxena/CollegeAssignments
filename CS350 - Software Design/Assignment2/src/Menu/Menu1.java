package Menu;

import IO.*;

public class Menu1 extends Menu{
//    ArrayList<String> options;


    public Menu1(){
//        options = new ArrayList<String>();
        this.options = new String[3];
        this.options[0] = "Survey";
        this.options[1] = "Test";
        this.options[2] = "Quit";
        this.numOfOptions = 3;
//        options.add("SurveyTest.Survey");
//        options.add("SurveyTest.Test");
    }

    public Menu1(String[] o){//ArrayList<String> o){
        this.options = o;
        this.numOfOptions = o.length;
    }



    public void callFunctions(int i){
        switch (i){
            case 1:
                SurveyMenu2 surveyMenu2 = new SurveyMenu2();
                surveyMenu2.executeMenu();
                break;
            case 2:
                TestMenu2 testMenu2 = new TestMenu2();
                testMenu2.executeMenu();
                break;
            case 3:
                Output.printString("Goodbye.");
                System.exit(0);
            default:
                Output.printString("This shouldn't be printed, something's wrong in the code.");
                break;
        }
        return;
    }
}
