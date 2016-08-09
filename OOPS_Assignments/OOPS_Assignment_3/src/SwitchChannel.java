import java.util.Scanner;

//Single responsibility Class (S-SOLID) : handles channel switching operation

public class SwitchChannel implements Functionality {
    public StateHandler runFunctionality(StateHandler state){

        if(state.isSwitchedOn == true){

            Scanner in = new Scanner(System.in);

            System.out.println("Enter channel to switch :");
            int channel = in.nextInt();

            if(channel<0 || channel>= state.maxChannelLimit){
                System.out.println("Invalid channel.\n");
            }else{
                state.channel = channel;
                System.out.println("Current channel :" + Integer.toString(state.channel)+"\n");
            }

        }else{
            System.out.println("First switch on the TV.\n");
        }

        return state;
    }
}
