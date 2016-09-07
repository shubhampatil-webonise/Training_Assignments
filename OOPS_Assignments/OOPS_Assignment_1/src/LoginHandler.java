import java.util.ArrayList;
import java.util.Scanner;

//Single responsibility Class (S-SOLID) : Handles only process flow of login

public class LoginHandler {

    public static void main(String args[]){

        Scanner in = new Scanner(System.in);

        //Instead of options, in real scenario buttons will be present.
        System.out.println("Login Options:\n1.Proprietor Login\t2.Facebook Login\t3.Twitter Login\t4.LinkedIn Login" +
                "\nEnter Proprietor, Facebook, Twitter or LinkedIn");

        String choice = in.next();

        DbConnector connector = new MySQLConnector();

        //Liskov's Substitution Principle (L - SOLID)
        LoginMethod loginMethod;

        switch (choice){
            case "Facebook" :   loginMethod = new FacebookLogin(connector);
                                loginMethod.login();
                                break;

            case "Twitter" :    loginMethod = new TwitterLogin(connector);
                                loginMethod.login();
                                break;

            case "LinkedIn" :   loginMethod = new LinkedinLogin(connector);
                                loginMethod.login();
                                break;

            case "Proprietor" : loginMethod = new ProprietorLogin(connector);
                                loginMethod.login();
                                break;

            default :   System.out.println("Wrong Input !");
                        break;
        }

    }
}
