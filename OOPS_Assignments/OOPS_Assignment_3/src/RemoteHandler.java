import java.util.ArrayList;
import java.util.Scanner;

//Single responsibility Class (S-SOLID) : handles control flow of the TV
public class RemoteHandler {

    public static void main(String args[]){


        System.out.println("Hey ! This is a TV");

        StateHandler newTVState = new TVState();
        Functionality functionality;

        System.out.println("Max Volume :" + Integer.toString(newTVState.maxVolumeLimit));
        System.out.println("Max Channels :" + Integer.toString(newTVState.maxChannelLimit));

        System.out.println("Use this remote to operate it.");

        Scanner in = new Scanner(System.in);

        while(true){
            System.out.println("1. Switch On/Off\n" +
                    "2. Channel Up\n" +
                    "3. Channel Down\n" +
                    "4. Volume Up\n" +
                    "5. Volume Down\n" +
                    "6. Switch Channel\n" +
                    "Choice :");

            int choice = in.nextInt();

            switch (choice) {
                case 1 :    functionality = new Switch();
                            newTVState = functionality.runFunctionality(newTVState);
                            break;

                case 2 :    functionality = new ChannelUp();
                            newTVState = functionality.runFunctionality(newTVState);
                            break;

                case 3 :    functionality = new ChannelDown();
                            newTVState = functionality.runFunctionality(newTVState);
                            break;

                case 4 :    functionality = new VolumeUp();
                            newTVState = functionality.runFunctionality(newTVState);
                            break;

                case 5 :    functionality = new VolumeDown();
                            newTVState = functionality.runFunctionality(newTVState);
                            break;

                case 6 :    functionality = new SwitchChannel();
                            newTVState = functionality.runFunctionality(newTVState);
                            break;

                default:    System.out.println("Wrong choice !\n");
                            break;
            }

        }
    }
}
