package SurveyTest;

import IO.FileLoader;
import IO.Output;
import IO.Response;
import Question.*;

import java.io.File;
import java.io.FileInputStream;
import java.io.ObjectInputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class Tabulator {
    public Tabulator(){}

    public static void tabulateSurvey(String surveyName){
        String path = "./Surveys/taken/" + surveyName + "/";
        ArrayList<Survey> surveys = new ArrayList<Survey>();
        FileLoader fileLoader = new FileLoader();

        File folder = new File(path);
        File[] files = folder.listFiles();
        ArrayList<String> fileNames = new ArrayList<String>();
        for (File file : files) {
            String fileName = file.getName();
            if(fileName.endsWith(".survey")){
                fileNames.add(fileName.substring(0,fileName.length() - 7));
            }
        }

        for (String fileName : fileNames){
            try {
                Survey survey = fileLoader.loadSurvey(fileName, path);
                surveys.add(survey);
            }
            catch (Exception e){
                Output.printString("eh");
            }
        }

        for(int i = 0; i<surveys.get(0).getNumberOfQuestions(); i++){
            HashMap<Response, Integer> responseIntegerHashMap = new HashMap<Response, Integer>();
            ArrayList<Response> responses = new ArrayList<Response>();
            for(Survey survey : surveys){
                Response response = survey.getQuestion(i).getResponse();
                if(responseIntegerHashMap.containsKey(response)){
                    responseIntegerHashMap.put(response, responseIntegerHashMap.get(response) + 1);
                }
                else{
                    responseIntegerHashMap.put(response,1);
                    responses.add(response);
                }
            }
            surveys.get(0).getQuestion(i).displayQuestion();

            for (Response response : responses){
                Output.printString("\n"+responseIntegerHashMap.get(response).toString());
                response.displayResponse();
            }
        }
    }

    public static void tabulateTest(String testName){
        String path = "./Tests/taken/" + testName + "/";
        ArrayList<Test> tests = new ArrayList<Test>();
        FileLoader fileLoader = new FileLoader();

        File folder = new File(path);
        File[] files = folder.listFiles();
        ArrayList<String> fileNames = new ArrayList<String>();
        for (File file : files) {
            String fileName = file.getName();
            if(fileName.endsWith(".test")){
                fileNames.add(fileName.substring(0,fileName.length() - 5));
            }
        }

        for (String fileName : fileNames){
            try {
                Test test = fileLoader.loadTest(fileName, path);
                tests.add(test);
            }
            catch (Exception e){
                Output.printString("eh");
            }
        }

        for(int i = 0; i<tests.get(0).getNumberOfQuestions(); i++){
            HashMap<Response, Integer> responseIntegerHashMap = new HashMap<Response, Integer>();
            ArrayList<Response> responses = new ArrayList<Response>();
            for(Test test : tests){
                Response response = test.getQuestion(i).getResponse();
                if(responseIntegerHashMap.containsKey(response)){
                    responseIntegerHashMap.put(response, responseIntegerHashMap.get(response) + 1);
                }
                else{
                    responseIntegerHashMap.put(response,1);
                    responses.add(response);
                }
            }
            tests.get(0).getQuestion(i).displayQuestion();

            for (Response response : responses){
                Output.printString("\n"+responseIntegerHashMap.get(response).toString());
                response.displayResponse();
            }
        }
    }
//
//    public static void tabulateSurveyQuestion(ArrayList<Question> questions){
//        Question firstQuestion = questions.get(0);
//        firstQuestion.displayQuestion();
//        if(firstQuestion instanceof EssayQ){
//            for(Question essayQ : questions){
//                essayQ.displayResponse();
//            }
//        }
//        else if(firstQuestion instanceof ShortAnswerQ){
//
//        }
//    }
//
//    public static void tabulateResponses(ArrayList<Response> responses){
//        ArrayList<Response> distinctResponses = new ArrayList<Response>();
//        for(Response response : responses){
//            if(!distinctResponses.contains(response)){
//                distinctResponses.add(response);
//            }
//        }
//    }
}
