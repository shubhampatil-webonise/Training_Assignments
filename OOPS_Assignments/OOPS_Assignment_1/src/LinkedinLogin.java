import java.util.Scanner;

//Single responsibility Class (S-SOLID) : Handles only LinkedIn login

public class LinkedinLogin implements LoginInterface{

    //Dependency Inversion (D-SOLID) : Instead of depending of MySQLConnector directly,
    //connecting to db using an abstract DbConnector interface
    DbConnector connector;
    String method;

    LinkedinLogin(String method, DbConnector connector){
        this.method = method;
        this.connector = connector;
    }

    public void login() {

        //check if current login method in LinkedIn
        if(this.method.equals("LinkedIn")){
            Scanner in = new Scanner(System.in);

            System.out.println("Enter your LinkedIn username :");
            String username = in.next();

            System.out.println("Enter your LinkedIn password :");
            String password = in.next();


            System.out.println("Success : Logged In !");

        }
    }
}
