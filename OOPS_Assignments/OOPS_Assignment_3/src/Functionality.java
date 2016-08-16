//Open for extension (O-SOLID) : new functionalities can be implemented using
//Functionality interface

//Interface Segeragation (I-SOLID) : interface to handles only functionalities
public interface Functionality {
    public StateHandler runFunctionality(StateHandler state);
}
