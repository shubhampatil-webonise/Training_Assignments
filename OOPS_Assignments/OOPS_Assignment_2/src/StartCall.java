import java.util.Scanner;

//Single Responsibility Class (S-SOLID) : Handles calling functionality

public class StartCall implements Functionality {

    public StateHandler runFunctionality(StateHandler state){

        if (state.isCalledEngaged == false && state.isUnlocked == true){

            Scanner in = new Scanner(System.in);
            System.out.println("Who do you want to call ?");
            String contact = in.next();


            System.out.println("Calling " + contact + " ! Call engaged.\n");
            state.isCalledEngaged = true;

        }else{

            if(state.isUnlocked == false){
                System.out.println("Unlock the mobile first.\n");
            }else{
                System.out.println("Engaged on another call.\n");
            }
        }

        return state;
    }
}
