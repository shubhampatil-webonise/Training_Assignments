import java.util.ArrayList;
import java.util.Scanner;

//Single Responsibility Class (S-SOLID) : Handles workflow of mobile

public class MobileHandler {
    public static void main(String args[]){

        Scanner in = new Scanner(System.in);

        StateHandler stateOfMobile = new StateHandler();

        Functionality functionality;

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

            switch (choice){
                case 1 :    functionality = new Unlock();
                            stateOfMobile = functionality.runFunctionality(stateOfMobile);
                            break;

                case 2 :    functionality = new Lock();
                            stateOfMobile = functionality.runFunctionality(stateOfMobile);
                            break;

                case 3 :    functionality = new StartCall();
                            stateOfMobile = functionality.runFunctionality(stateOfMobile);
                            break;

                case 4 :    functionality = new EndCall();
                            stateOfMobile = functionality.runFunctionality(stateOfMobile);
                            break;

                case 5 :    functionality = new SendMessage();
                            stateOfMobile = functionality.runFunctionality(stateOfMobile);
                            break;

                case 6 :    functionality = new Camera();
                            stateOfMobile = functionality.runFunctionality(stateOfMobile);
                            break;

                case 7 :    functionality = new Internet();
                            stateOfMobile = functionality.runFunctionality(stateOfMobile);
                            break;

                default:    System.out.println("Wrong input !\n");
                            break;
            }
        }

    }
}
