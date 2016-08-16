
//Open for extension (O-SOLID) : provides interface which can be implemented for a new database connection
//without modifying the existing code.

//Interface Segeragation (I-SOLID) : provides a segeragated interface from other interfaces

public interface DbConnector {
    public void connectToDb();
}
