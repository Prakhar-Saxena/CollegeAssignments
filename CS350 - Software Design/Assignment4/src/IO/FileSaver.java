package IO;

import SurveyTest.*;

import java.io.*;

public class FileSaver {
    protected final String surveyPath = "./Surveys/taken/";
    protected final String surveyTemplatePath = "./Surveys/templates/";
    protected final String surveyExtension = ".survey";
    protected final String testPath = "./Tests/taken/";
    protected final String testTemplatePath = "./Tests/templates/";
    protected final String testExtension = ".test";


//            File file = new File(this.surveyPath+name+this.surveyExtension);
//            file.createNewFile();

    public void saveSurveyTemplate(Survey survey, String name) throws FileNotFoundException, IOException{
//        try{
        FileOutputStream fileOutputStream = new FileOutputStream(this.surveyTemplatePath+name+this.surveyExtension);
        ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);
        objectOutputStream.writeObject(survey);
        objectOutputStream.close();
        fileOutputStream.close();
//        }
//        catch (Exception e){
//            e.getStackTrace();
//            Output.printError(e.toString());
//        }
    }

    public void saveSurvey(Survey survey, String name, String path) throws FileNotFoundException, IOException{
        File file = new File(path);
        file.mkdir();
        FileOutputStream fileOutputStream = new FileOutputStream(path+name+".survey");
        ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);
        objectOutputStream.writeObject(survey);
        objectOutputStream.close();
        fileOutputStream.close();


    }

    public void saveTestTemplate(Test test, String name) throws FileNotFoundException, IOException{
//        try{
        FileOutputStream fileOutputStream = new FileOutputStream(this.testTemplatePath+name+this.testExtension);
        ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);
        objectOutputStream.writeObject(test);
        objectOutputStream.close();
        fileOutputStream.close();
//        }
//        catch (Exception e){
//            e.getStackTrace();
//            Output.printString(e.toString());
//        }
    }

    public void saveTest(Test test, String name, String path) throws FileNotFoundException, IOException{
//        try{
        File file = new File(path);
        file.mkdir();
        FileOutputStream fileOutputStream = new FileOutputStream(path+name+".test");
        ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);
        objectOutputStream.writeObject(test);
        objectOutputStream.close();
        fileOutputStream.close();
//        }
//        catch (Exception e){
//            e.getStackTrace();
//            Output.printString(e.toString());
//        }
    }
}
