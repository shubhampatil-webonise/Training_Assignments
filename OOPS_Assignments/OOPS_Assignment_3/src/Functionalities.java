import java.util.ArrayList;

//Single responsibility Class (S-SOLID) : returns collective functionalities of the remote

public class Functionalities {

    ArrayList<Functionality> functionalities;

    Functionalities(){
        this.functionalities = new ArrayList<Functionality>();
    }

    public ArrayList<Functionality> allFunctionalities(){

        //Liskov's Substitution (L-SOLID) : parent class used in place of child classes
        this.functionalities.add(new Switch());
        this.functionalities.add(new ChannelUp());
        this.functionalities.add(new ChannelDown());
        this.functionalities.add(new VolumeUp());
        this.functionalities.add(new VolumeDown());
        this.functionalities.add(new SwitchChannel());

        return this.functionalities;
    }
}
