import java.util.ArrayList;
import java.util.Scanner;

//Single Responsibility Class (S-SOLID) : Handles workflow of mobile

public class MobileHandler {
    public static void main(String args[]){

        Scanner in = new Scanner(System.in);

        StateHandler stateOfMobile = new StateHandler();

        while(true){
            System.out.println("Select a function:" +
                    "\n1. Unlock Phone" +
                    "\n2. Lock Phone" +
                    "\n3. Make a call" +
                    "\n4. End a call" +
                    "\n5. Send a message" +
                    "\n6. Use Camera" +
                    "\n7. Use Internet" +
                    "\nChoice : ");


            int choice = in.nextInt();

            ArrayList<Functionality> functionalities = new GetFunctionalities().supplyFunctionalities();

            stateOfMobile = functionalities.get(choice - 1).runFunctionality(stateOfMobile);
        }

    }
}
