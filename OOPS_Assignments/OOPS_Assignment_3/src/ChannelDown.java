//Single responsibility Class (S-SOLID) : handles channel down operation

public class ChannelDown implements Functionality {
    public StateHandler runFunctionality(StateHandler state){

        if(state.isSwitchedOn == true){

            if(state.channel < 0){
                state.channel = state.maxChannelLimit + state.channel + 1;

            }else{
                state.channel = state.channel - 1;
            }

            System.out.println("Current channel :" + Integer.toString(state.channel)+"\n");

        }else{
            System.out.println("First switch on the TV.\n");
        }

        return state;
    }
}
