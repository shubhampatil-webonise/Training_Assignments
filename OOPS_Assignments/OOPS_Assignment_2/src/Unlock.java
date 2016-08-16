//Single Responsibility Class (S-SOLID) : Handles mobile unlocking functionality

public class Unlock implements Functionality {
    public StateHandler runFunctionality(StateHandler state){

        if (state.isUnlocked == true){
            System.out.println("Mobile is already unlocked.\n");
        }else{

            state.isUnlocked = true;

            System.out.println("Mobile unlocked.\n");

        }

        return state;
    }
}
