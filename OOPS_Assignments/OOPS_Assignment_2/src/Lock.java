//Single Responsibility Class (S-SOLID) : Handles mobile locking functionality

public class Lock implements Functionality{
    public StateHandler runFunctionality(StateHandler state){

        if (state.isUnlocked == false){
            System.out.println("Mobile is already locked.\n");
        }else{

            state.isUnlocked = false;

            System.out.println("Mobile locked.\n");
        }

        return state;
    }
}
