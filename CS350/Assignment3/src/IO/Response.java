package IO;

import java.io.Serializable;
import java.util.ArrayList;

public class Response implements Serializable {
    ArrayList<String> stringResponse;

    public Response(){
        this.stringResponse = new ArrayList<String>();
    }

    public Response(String string){
        this.stringResponse = new ArrayList<String>();
        this.stringResponse.add(string);
    }

    public Response(ArrayList<String> strings){
        this.stringResponse = new ArrayList<String>();
        this.stringResponse = strings;
    }

    public String getResponseAsString(){
        String resp = "";
        for (String i : this.stringResponse){
            resp += i;
        }
        return resp;
    }

    public int getResponseSize(){
        return this.stringResponse.size();
    }

    public ArrayList<String> getResponseAsArrayList(){
        return this.stringResponse;
    }

    public void displayResponse(){
        Output.printString("Response:");
        Output.printStringArrayList(this.stringResponse);
    }

    public void addResponse(String string){
        stringResponse.add(string);
    }
}
