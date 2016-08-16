import java.util.Scanner;

//Single Responsibility Class (S-SOLID) : Handles internet functionality

public class Internet implements Functionality {
    public StateHandler runFunctionality(StateHandler state){

        if(state.isUnlocked == true){
            Scanner in = new Scanner(System.in);

            System.out.println("Enter Url :");
            String url = in.next();

            System.out.println("Enter search query :");
            String searchQuery = in.next();

            //do actual search here.

            System.out.println(url + " replied : Hey !\n");

        }else{
            System.out.println("Unlock the mobile first.\n");
        }

        return state;
    }
}
