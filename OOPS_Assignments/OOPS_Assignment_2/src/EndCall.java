import java.util.Scanner;

//Single Responsibility Class (S-SOLID) : Handles call termination

public class EndCall implements Functionality {

    public StateHandler runFunctionality(StateHandler state){

        if (state.isCalledEngaged == true && state.isUnlocked == true){

            state.isCalledEngaged = false;
            System.out.println("Disconnecting Call.\n");
        }else{

            if(state.isUnlocked == false){
                System.out.println("Unlock the mobile first.\n");
            }else{
                System.out.println("Mobile not engaged on any call.\n");
            }
        }

        return state;
    }

}
