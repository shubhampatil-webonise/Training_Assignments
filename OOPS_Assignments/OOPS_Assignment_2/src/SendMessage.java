import java.util.Scanner;

//Single Responsibility Class (S-SOLID) : Handles messaging functionality

public class SendMessage implements Functionality {

    public StateHandler runFunctionality(StateHandler state){

        if(state.isUnlocked == true){
            Scanner in = new Scanner(System.in);

            System.out.println("Enter contact : ");
            String contact = in.next();

            System.out.println("Message to send ? :");
            String message = in.next();

            System.out.println("Sending '" + message + "' to " + contact+"\n");

        }else{
            System.out.println("Unlock the phone first.\n");

        }

        return state;
    }
}
