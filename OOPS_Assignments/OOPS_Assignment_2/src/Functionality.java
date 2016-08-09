//Open for extension (O-SOLID) : new functionalities can be implemented
//using Functionality interface

//Interface segeragation (I-SOLID)
public interface Functionality {
    public StateHandler runFunctionality(StateHandler state);
}
