package IO;

import SurveyTest.*;

import IO.Output;

import java.io.FileInputStream;
import java.io.ObjectInputStream;

public class FileLoader {
    protected final String surveyPath = "./Surveys/";
    protected final String surveyExtension = ".survey";
    protected final String testPath = "./Tests/";
    protected final String testExtension = ".test";

    public Survey loadSurvey(String name){
        try{
            FileInputStream fileInputStream = new FileInputStream(this.surveyPath+name+this.surveyExtension);
            ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream);
            Survey survey = (Survey) objectInputStream.readObject();
            objectInputStream.close();
            fileInputStream.close();
            return survey;
        }
        catch (Exception e){
            Output.printString("File Not Found. (Probably)");
            e.printStackTrace();
            return null;
        }
    }

    public Test loadTest(String name){
        try{
            FileInputStream fileInputStream = new FileInputStream(this.testPath+name+this.testExtension);
            ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream);
            Test test= (Test) objectInputStream.readObject();
            objectInputStream.close();
            fileInputStream.close();
            return test;
        }
        catch (Exception e){
            Output.printString("File Not Found. (Probably)");
            e.printStackTrace();
            return null;
        }
    }
}
