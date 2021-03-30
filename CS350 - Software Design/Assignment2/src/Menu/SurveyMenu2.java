package Menu;

import IO.*;
import SurveyTest.*;

import java.io.File;
import java.util.ArrayList;

public class SurveyMenu2 extends Menu {
    protected Survey surveyInMemory;
    protected String surveyName;

    public SurveyMenu2(){
        this.options = new String[5];
        this.options[0] = "Create a new Survey";
        this.options[1] = "Display a Survey";
        this.options[2] = "Load a Survey";
        this.options[3] = "Save a Survey";
        this.options[4] = "Quit";
        this.numOfOptions = 5;
        this.surveyInMemory =  new Survey();
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
        return;
    }

    public void create(){
        Output.printString("Enter A Name: ");
        this.surveyName = Input.getInputString();
        this.surveyInMemory = new Survey();
        surveyInMemory = Survey.create(this.surveyName);
        SurveyMenu3 surveyMenu3 = new SurveyMenu3(this.surveyInMemory);
        this.surveyInMemory = surveyMenu3.returnSurvey();//this.surveyInMemory);
//        surveyMenu3.executeMenu();
    }

    public void display(){
        this.surveyInMemory.displaySurvey();
    }

    public void load(){
        File folder = new File("./Surveys/");
        File[] files = folder.listFiles();
        ArrayList<String> fileNames = new ArrayList<String>();
        for (File file : files) {
            String fileName = file.getName();
            if(fileName.endsWith(".survey")){
                fileNames.add(fileName.substring(0,fileName.length() - 7));
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
        this.surveyInMemory = fileLoader.loadSurvey(fileNames.get(input-1));
        Output.printString("Survey Loaded.");
    }

    public void save(){
        FileSaver fileSaver = new FileSaver();
        fileSaver.saveSurvey(this.surveyInMemory, this.surveyName);
        Output.printString("Survey Saved.");
    }

    public void quit(){
        Output.printString("Goodbye.");
        System.exit(0);
    }
}
