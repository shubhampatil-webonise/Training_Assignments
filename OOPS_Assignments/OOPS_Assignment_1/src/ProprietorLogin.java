import java.util.Scanner;

//Single responsibility Class (S-SOLID) : Handles only Proprietor login

public class ProprietorLogin implements LoginMethod {

    //Dependency Inversion (D-SOLID) : Instead of depending of MySQLConnector directly,
    //connecting to db using an abstract DbConnector interface
    DbConnector connector;

    ProprietorLogin(DbConnector connector){
        this.connector = connector;
    }

    public void login(){

        Scanner in = new Scanner(System.in);

        System.out.println("Enter your Proprietor username :");
        String username = in.next();

        System.out.println("Enter your Proprietor password :");
        String password = in.next();

        connector.connectToDb();

        System.out.println("Success : Logged In !");
    }
}
