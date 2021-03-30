package Menu;

import IO.*;
import SurveyTest.*;

import java.io.File;
import java.util.ArrayList;

public class TestMenu2 extends Menu1 {
    protected Test testTemplateInMemory;
    protected String testTemplateName;
    protected Test testTake;
    protected String testTakeName;
//    String[] options = {"Create a new SurveyTest.Test", "Display a SurveyTest.Test", "Load a SurveyTest.Test", "Save a SurveyTest.Test", "Quit"};
//    protected final int numOfOptions = 5;

    public TestMenu2(){
        this.options = new String[9];
        this.options[0] = "Create a new Test";
        this.options[1] = "Display a Test";
        this.options[2] = "Load a Test";
        this.options[3] = "Save a Test Template";
        this.options[4] = "Modify a Test";
        this.options[5] = "Take a Test";
        this.options[6] = "Tabulate a Test";
        this.options[7] = "Grade a Test";
        this.options[8] = "Quit";
        this.numOfOptions = 9;
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
                saveTemplate();
                break;
            case 5:
                modify();
                break;
            case 6:
                take();
                break;
            case 7:
                tabulate();
                break;
            case 8:
                grade();
                break;
            case 9:
                return;
            default:
                break;
        }
    }



    public void create(){
        Output.printString("Enter A Name: ");
        this.testTemplateName = Input.getInputString();
        this.testTemplateInMemory = new Test();
        testTemplateInMemory = Test.create(this.testTemplateName);
        TestMenu3 testMenu3 = new TestMenu3(this.testTemplateInMemory);
        this.testTemplateInMemory = testMenu3.returnTest();//this.testInMemory);
    }

    public void display(){
        this.testTemplateInMemory.displayTest();
    }

    public void load(){
        File folder = new File("./Tests/templates/");
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
        while(true){
            try{
                this.testTemplateInMemory = fileLoader.loadTestTemplate(fileNames.get(input-1));
                this.testTemplateName = fileNames.get(input-1);
                break;
            }
            catch(Exception e){
                e.getStackTrace();
                Output.printString(e.toString());
            }
        }
        Output.printString("Test Loaded.");
    }

    public void saveTemplate(){
        FileSaver fileSaver = new FileSaver();
        while(true){
            try{
                fileSaver.saveTestTemplate(this.testTemplateInMemory, this.testTemplateName);
                break;
            }
            catch(Exception e){
                e.getStackTrace();
                Output.printString(e.toString());
            }
        }
        Output.printString("Test Saved.");
    }

    public void tabulate(){
        this.load();
        Tabulator tabulator = new Tabulator();
        tabulator.tabulateTest(this.testTemplateName);
    }

    public void take(){
        this.load();
        Output.printString("Enter a Name:");
        String name = Input.getInputString();
        this.testTakeName = name;
        String path = "./Tests/taken/"+this.testTemplateName+"/";
        this.testTake = this.testTemplateInMemory.takeTest();
        FileSaver fileSaver = new FileSaver();
        while(true){
            try{
                fileSaver.saveTest(this.testTake, this.testTakeName, path);
                break;
            }
            catch (Exception e){
                e.getStackTrace();
                Output.printString(e.toString());
                return;
            }
        }
        Output.printString("Test Saved.");
        Output.printString("You got: "+this.testTake.getGrade()+"/"+this.testTake.getMaxGrade());
    }

    public void grade(){
        this.load();
        File folder = new File("./Tests/taken/"+this.testTemplateName+"/");
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
        while(true){
            try{
                String path = "./Tests/taken/"+this.testTemplateName+"/";
                this.testTake = fileLoader.loadTest(fileNames.get(input-1),path);
                break;
            }
            catch(Exception e){
                e.getStackTrace();
                Output.printString(e.toString());
            }
        }
        Output.printString("Test Loaded.");
        this.testTake.gradeTest();
        Output.printString(this.testTake.getGrade()+"/"+this.testTake.getMaxGrade());
    }

    public void modify(){
        this.load();
        TestModifier testModifier = new TestModifier(this.testTemplateInMemory);
        testModifier.ModifyTestQuestions();
    }

    public void quit(){
        Output.printString("Goodbye.");
        System.exit(0);
    }
}
