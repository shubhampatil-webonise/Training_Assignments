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


        //to avoid if-else statements, get all available loginMethods and call login for each loginMethod
        ArrayList<LoginInterface> loginMethods = new LoginMethods().supplyLoginMethods(choice);

        for(LoginInterface method : loginMethods){
            method.login();
        }
    }
}
