package IO;

import SurveyTest.*;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;

public class FileLoader {
    protected final String surveyPath = "./Surveys/";
    protected final String surveyTemplatePath = surveyPath + "templates/";
    protected final String surveyExtension = ".survey";
    protected final String testPath = "./Tests/";
    protected final String testTemplatePath = testPath + "templates/";
    protected final String testExtension = ".test";

    public Survey loadSurveyTemplate(String name)throws FileNotFoundException, IOException, ClassNotFoundException {
//        try{
        FileInputStream fileInputStream = new FileInputStream(this.surveyTemplatePath+name+this.surveyExtension);
        ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream);
        Survey survey = (Survey) objectInputStream.readObject();
        objectInputStream.close();
        fileInputStream.close();
        return survey;
//        }
//        catch (Exception e){
//            Output.printString("File Not Found. (Probably)");
//            e.printStackTrace();
//            return null;
//        }
    }

    public Survey loadSurvey(String name, String path)throws FileNotFoundException, IOException, ClassNotFoundException{
//        try{
        FileInputStream fileInputStream = new FileInputStream(path+name+this.surveyExtension);
        ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream);
        Survey survey = (Survey) objectInputStream.readObject();
        objectInputStream.close();
        fileInputStream.close();
        return survey;
//        }
//        catch (Exception e){
//            Output.printString("File Not Found. (Probably)");
//            e.printStackTrace();
//            return null;
//        }
    }

    public Test loadTestTemplate(String name)throws FileNotFoundException, IOException, ClassNotFoundException{
//        try{
        FileInputStream fileInputStream = new FileInputStream(this.testTemplatePath+name+this.testExtension);
        ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream);
        Test test= (Test) objectInputStream.readObject();
        objectInputStream.close();
        fileInputStream.close();
        return test;
//        }
//        catch (Exception e){
//            Output.printString("File Not Found. (Probably)");
//            e.printStackTrace();
//            return null;
//        }
    }

    public Test loadTest(String name, String path)throws FileNotFoundException, IOException, ClassNotFoundException{
//        try{
        FileInputStream fileInputStream = new FileInputStream(path+name+this.testExtension);
        ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream);
        Test test= (Test) objectInputStream.readObject();
        objectInputStream.close();
        fileInputStream.close();
        return test;
//        }
//        catch (Exception e){
//            Output.printString("File Not Found. (Probably)");
//            e.printStackTrace();
//            return null;
//        }
    }
}
