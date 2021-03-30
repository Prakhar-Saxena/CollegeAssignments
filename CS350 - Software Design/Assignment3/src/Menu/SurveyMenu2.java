package Menu;

import IO.*;
import SurveyTest.*;

import java.io.File;
import java.util.ArrayList;

public class SurveyMenu2 extends Menu {
    protected Survey surveyTemplateInMemory;
    protected String surveyTemplateName;
    protected Survey surveyTake;
    protected String surveyTakeName;

    public SurveyMenu2(){
        this.options = new String[8];
        this.options[0] = "Create a new Survey";
        this.options[1] = "Display a Survey";
        this.options[2] = "Load a Survey";
        this.options[3] = "Save a Survey Template";
        this.options[4] = "Modify an Existing Survey";
        this.options[5] = "Take a Survey";
        this.options[6] = "Tabulate a Survey";
        this.options[7] = "Quit";
        this.numOfOptions = 8;
        this.surveyTemplateInMemory =  new Survey();
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
                return;
            default:
                break;
        }
        return;
    }

    public void create(){
        Output.printString("Enter A Name: ");
        this.surveyTemplateName = Input.getInputString();
        this.surveyTemplateInMemory = new Survey();
        surveyTemplateInMemory = Survey.create(this.surveyTemplateName);
        SurveyMenu3 surveyMenu3 = new SurveyMenu3(this.surveyTemplateInMemory);
        this.surveyTemplateInMemory = surveyMenu3.returnSurvey();//this.surveyInMemory);
//        surveyMenu3.executeMenu();
    }

    public void display(){
        this.surveyTemplateInMemory.displaySurvey();
    }

    public void load(){
        File folder = new File("./Surveys/templates/");
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
        while(true){
            try{
                this.surveyTemplateInMemory = fileLoader.loadSurveyTemplate(fileNames.get(input-1));
                this.surveyTemplateName = fileNames.get(input-1);
                break;
            }
            catch (Exception e){
                e.getStackTrace();
                Output.printString(e.toString());
            }
        }

        Output.printString("Survey Loaded.");
    }

    public void saveTemplate(){
        FileSaver fileSaver = new FileSaver();
        while(true){
            try {
                fileSaver.saveSurveyTemplate(this.surveyTemplateInMemory, this.surveyTemplateName);
                break;
            } catch (Exception e) {
                e.getStackTrace();
                Output.printString(e.toString());
                return;
            }
        }
        Output.printString("Survey Saved.");
    }

    public void modify(){
        this.load();
        SurveyModifier surveyModifier = new SurveyModifier(this.surveyTemplateInMemory);
        surveyModifier.ModifySurveyQuestions();
    }

    public void take(){
        this.load();
        Output.printString("Enter a Name:");
        String name = Input.getInputString();
        this.surveyTakeName = name;
        String path = "./Surveys/taken/"+this.surveyTemplateName+"/";
        this.surveyTake = this.surveyTemplateInMemory.takeSurvey();
        FileSaver fileSaver = new FileSaver();
        while(true){
            try{
                fileSaver.saveSurvey(this.surveyTake, this.surveyTakeName, path);
                break;
            }
            catch (Exception e){
                e.getStackTrace();
                Output.printString(e.toString());
                return;
            }
        }
        Output.printString("Survey Saved.");
    }

    public void tabulate(){
        this.load();
        Tabulator tabulator = new Tabulator();
        tabulator.tabulateSurvey(this.surveyTemplateName);
    }

    public void quit(){
        Output.printString("Goodbye.");
        System.exit(0);
    }
}
