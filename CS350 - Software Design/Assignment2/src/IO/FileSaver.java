package IO;

import SurveyTest.*;

import java.io.*;

public class FileSaver {
    protected final String surveyPath = "./Surveys/";
    protected final String surveyExtension = ".survey";
    protected final String testPath = "./Tests/";
    protected final String testExtension = ".test";

    public void saveSurvey(Survey survey, String name) {
        try{
//            File file = new File(this.surveyPath+name+this.surveyExtension);
//            file.createNewFile();
            FileOutputStream fileOutputStream = new FileOutputStream(this.surveyPath+name+this.surveyExtension);
            ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);
            objectOutputStream.writeObject(survey);
            objectOutputStream.close();
            fileOutputStream.close();
        }
        catch (Exception e){
            e.getStackTrace();
            Output.printError(e.toString());
        }
    }

    public void saveTest(Test test, String name) {
        try{
            FileOutputStream fileOutputStream = new FileOutputStream(this.testPath+name+this.testExtension);
            ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);
            objectOutputStream.writeObject(test);
            objectOutputStream.close();
            fileOutputStream.close();
        }
        catch (Exception e){
            e.getStackTrace();
            Output.printError(e.toString());
        }
    }
}
