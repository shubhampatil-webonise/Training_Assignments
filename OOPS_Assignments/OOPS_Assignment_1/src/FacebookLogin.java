import java.util.Scanner;

//Single responsibility Class (S-SOLID) : Handles only Facebook login

public class FacebookLogin implements LoginMethod {


    //Dependency Inversion (D-SOLID) : Instead of depending of MySQLConnector directly,
    //connecting to db using an abstract DbConnector interface
    DbConnector connector;

    FacebookLogin(DbConnector connector){
        this.connector = connector;
    }

    public void login(){

        Scanner in = new Scanner(System.in);

        System.out.println("Enter your Facebook username :");
        String username = in.next();

        System.out.println("Enter your Facebook password :");
        String password = in.next();

        connector.connectToDb();

        System.out.println("Success : Logged In !");
    }

}
