import java.util.Scanner;

//Single responsibility Class (S-SOLID) : Handles only Twitter login

public class TwitterLogin implements LoginInterface{

    //Dependency Inversion (D-SOLID) : Instead of depending of MySQLConnector directly,
    //connecting to db using an abstract DbConnector interface
    DbConnector connector;
    String method;

    TwitterLogin(String method, DbConnector connector){
        this.method = method;
        this.connector = connector;
    }

    public void login(){

        //check if current login method is Twitter
        if (this.method.equals("Twitter")){
            Scanner in = new Scanner(System.in);

            System.out.println("Enter your Twitter username :");
            String username = in.next();

            System.out.println("Enter your Twitter password :");
            String password = in.next();

            connector.connectToDb();

            System.out.println("Success : Logged In !");
        }
    }
}
