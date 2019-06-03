package Menu;

import IO.*;

public abstract class Menu {
    protected String[] options;
    protected int numOfOptions;
    protected final String invalidInputResponse = "Invalid IO.Input. Please Enter again.";

    public void executeMenu() {
        try{
            int input;
            while(true){
                displayMenu();
                input = Input.getInputInteger();
                if (input == numOfOptions){ //if quit is selected
                    callFunctions(input);
                    return;
                }
                else if (input >= 1 && input < this.numOfOptions){
                    callFunctions(input);
                }
                else{
                    Output.printString(this.invalidInputResponse);
                }
            }
//            return;
        }
        catch (Exception e){
            Output.printError(e.toString());
            Output.printString(this.invalidInputResponse);
            executeMenu();
        }
    }



    public void displayMenu(){
        for(int i = 0; i < this.options.length; i++){//options.size(); i++){
            String menuString = i+1+") "+ this.options[i];//.get(i);
            Output.printString(menuString);
        }
    }

    public abstract void callFunctions(int i);
}
