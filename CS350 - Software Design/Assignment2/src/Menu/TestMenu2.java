package Menu;

import IO.*;
import SurveyTest.*;

import java.io.File;
import java.util.ArrayList;

public class TestMenu2 extends Menu1 {
    protected Test testInMemory;
    protected String testName;
//    String[] options = {"Create a new SurveyTest.Test", "Display a SurveyTest.Test", "Load a SurveyTest.Test", "Save a SurveyTest.Test", "Quit"};
//    protected final int numOfOptions = 5;

    public TestMenu2(){
        this.options = new String[5];
        this.options[0] = "Create a new Test";
        this.options[1] = "Display a Test";
        this.options[2] = "Load a Test";
        this.options[3] = "Save a Test";
        this.options[4] = "Quit";
        this.numOfOptions = 5;
    }

    public void callFunctions(int x){
        switch (x){
            case 1:
                create();
                break;
            case 2:
                display();
                break;
            case 3:
                load();
                break;
            case 4:
                save();
                break;
            case 5:
                return;
            default:
                break;
        }
    }



    public void create(){
        Output.printString("Enter A Name: ");
        this.testName = Input.getInputString();
        this.testInMemory = new Test();
        testInMemory = Test.create(this.testName);
        TestMenu3 testMenu3 = new TestMenu3(this.testInMemory);
        this.testInMemory = testMenu3.returnTest();//this.testInMemory);
    }

    public void display(){
        this.testInMemory.displayTest();
    }

    public void load(){
        File folder = new File("./Tests/");
        File[] files = folder.listFiles();
        ArrayList<String> fileNames = new ArrayList<String>();
        for (File file : files) {
            String fileName = file.getName();
            if(fileName.endsWith(".test")){
                fileNames.add(fileName.substring(0,fileName.length() - 5));
            }
        }
        Output.printString("Please select a file to load:");
        Output.printStringArrayListNumbered(fileNames);
        int input = Input.getInputInteger();
        while(!(input >= 1 && input <= fileNames.size())){
            Output.printString(this.invalidInputResponse);
            input = Input.getInputInteger();
        }
        FileLoader fileLoader = new FileLoader();
        this.testInMemory = fileLoader.loadTest(fileNames.get(input-1));
        Output.printString("Test Loaded.");
    }

    public void save(){
        FileSaver fileSaver = new FileSaver();
        fileSaver.saveTest(this.testInMemory, this.testName);
        Output.printString("Test Saved.");
    }

    public void quit(){
        Output.printString("Goodbye.");
        System.exit(0);
    }
}
