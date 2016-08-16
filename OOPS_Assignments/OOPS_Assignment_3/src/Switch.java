import java.util.Scanner;

//Single responsibility Class (S-SOLID) : handles tv on/off operation

public class Switch implements Functionality {

    public StateHandler runFunctionality(StateHandler state){

        if(state.isSwitchedOn == true){
            state.isSwitchedOn = false;
            System.out.println("Switched off the TV.\n");
        }else{
            state.isSwitchedOn = true;
            System.out.println("Switched on the TV.\n");
        }

        return state;
    }
}
