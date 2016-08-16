
//A low level module communicating with high level modules using an abstract DbConnector

public class MySQLConnector implements DbConnector {

    @Override
    public void connectToDb() {
        System.out.println("Sending to MySQL DB ...");
    }
}
