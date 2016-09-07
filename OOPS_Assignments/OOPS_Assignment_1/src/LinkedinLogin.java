import java.util.Scanner;

//Single responsibility Class (S-SOLID) : Handles only LinkedIn login

public class LinkedinLogin implements LoginMethod{

    //Dependency Inversion (D-SOLID) : Instead of depending of MySQLConnector directly,
    //connecting to db using an abstract DbConnector interface
    DbConnector connector;

    LinkedinLogin(DbConnector connector){
        this.connector = connector;
    }

    public void login() {

        Scanner in = new Scanner(System.in);

        System.out.println("Enter your LinkedIn username :");
        String username = in.next();

        System.out.println("Enter your LinkedIn password :");
        String password = in.next();


        System.out.println("Success : Logged In !");

    }
}
