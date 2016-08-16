//Single Responsibility Class (S-SOLID) : Handles camera functionality

public class Camera implements Functionality {

    public StateHandler runFunctionality(StateHandler state){

        if (state.isCameraOpen == false && state.isUnlocked == true){
            state.isCameraOpen = true;
            System.out.println("Opening Camera. Done.\n");

        }else{
            if(state.isUnlocked == false){
                System.out.println("Unlock the mobile first\n");
            }else{
                System.out.println("Camera is already open.\n");
            }
        }

        return state;
    }
}
