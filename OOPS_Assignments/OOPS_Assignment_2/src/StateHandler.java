//Single Responsibility Class (S-SOLID) : Handles state of mobile

public class StateHandler {

    boolean isUnlocked;
    boolean isCalledEngaged;
    boolean isCameraOpen;

    StateHandler(){
        this.isUnlocked = false;
        this.isCalledEngaged = false;
        this.isCameraOpen = false;
    }
}
