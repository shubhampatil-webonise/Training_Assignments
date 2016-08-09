//Single responsibility Class (S-SOLID) : handles channel up operation

public class ChannelUp implements Functionality {
    public StateHandler runFunctionality(StateHandler state){

        if(state.isSwitchedOn == true){

            if(state.channel >= state.maxChannelLimit){
                state.channel = state.channel%state.maxChannelLimit;

            }else{
                state.channel = state.channel + 1;
            }

            System.out.println("Current channel :" + Integer.toString(state.channel) +"\n");

        }else{
            System.out.println("First switch on the TV.\n");
        }

        return state;
    }
}
