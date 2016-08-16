import java.util.Scanner;

//Single responsibility Class (S-SOLID) : Handles only Facebook login

public class FacebookLogin implements LoginInterface {


    //Dependency Inversion (D-SOLID) : Instead of depending of MySQLConnector directly,
    //connecting to db using an abstract DbConnector interface
    DbConnector connector;
    String method;

    FacebookLogin(String method, DbConnector connector){
        this.method = method;
        this.connector = connector;
    }

    public void login(){

        //check if current login method is Facebook
        if (this.method.equals("Facebook")){
            Scanner in = new Scanner(System.in);

            System.out.println("Enter your Facebook username :");
            String username = in.next();

            System.out.println("Enter your Facebook password :");
            String password = in.next();

            connector.connectToDb();

            System.out.println("Success : Logged In !");
        }
    }

}
