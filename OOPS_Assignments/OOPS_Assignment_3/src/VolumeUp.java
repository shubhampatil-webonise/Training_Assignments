//Single responsibility Class (S-SOLID) : handles volume up operation

public class VolumeUp implements Functionality {
    public StateHandler runFunctionality(StateHandler state){

        if(state.isSwitchedOn == true){

            if(state.volume >= state.maxVolumeLimit){
                state.volume = state.maxVolumeLimit;

            }else{
                state.volume = state.volume + 1;
            }

            System.out.println("Current volume :" + Integer.toString(state.volume) +"\n");

        }else{
            System.out.println("First switch on the TV.\n");
        }

        return state;
    }

}
