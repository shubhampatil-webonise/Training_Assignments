import java.util.ArrayList;

//Single responsibility Class (S-SOLID) : Provides all available login methods

public class LoginMethods {

    public ArrayList<LoginInterface> supplyLoginMethods(String choice){

        ArrayList<LoginInterface> loginMethods = new ArrayList<LoginInterface>();

        DbConnector connector = new MySQLConnector();

        //Liskov's Substitution Principle (L-SOLID) : parent class used in place of child classes
        loginMethods.add(new FacebookLogin(choice, connector));
        loginMethods.add(new ProprietorLogin(choice, connector));
        loginMethods.add(new TwitterLogin(choice, connector));
        loginMethods.add(new LinkedinLogin(choice, connector));


        return loginMethods;

    }

}
