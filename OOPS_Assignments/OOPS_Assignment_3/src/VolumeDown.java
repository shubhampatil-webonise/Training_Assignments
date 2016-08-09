//Single responsibility Class (S-SOLID) : handles volume down operation

public class VolumeDown implements Functionality {
    public StateHandler runFunctionality(StateHandler state){

        if(state.isSwitchedOn == true){

            if(state.volume <= 0){
                state.volume = 0;
            }else{
                state.volume = state.volume - 1;
            }

            System.out.println("Current volume :" + Integer.toString(state.volume)+"\n");

        }else{
            System.out.println("First switch on the TV.\n");
        }

        return state;
    }
}
