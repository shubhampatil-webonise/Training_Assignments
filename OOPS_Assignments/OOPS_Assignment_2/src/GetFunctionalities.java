import java.util.ArrayList;

//Single Responsibility Class (S-SOLID) : returns all functions of mobile collectively

public class GetFunctionalities {

    ArrayList<Functionality> functionalities = new ArrayList<Functionality>();

    //Liskov's Substitution (L-SOLID) : Parent class used in place of Child class
    //Parent : Functionality
    public ArrayList<Functionality> supplyFunctionalities(){
        this.functionalities.add(new Unlock());
        this.functionalities.add(new Lock());
        this.functionalities.add(new StartCall());
        this.functionalities.add(new EndCall());
        this.functionalities.add(new SendMessage());
        this.functionalities.add(new Camera());
        this.functionalities.add(new Internet());

        return this.functionalities;
    }
}
