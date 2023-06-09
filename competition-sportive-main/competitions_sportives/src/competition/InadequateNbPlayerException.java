package competition;

public class InadequateNbPlayerException extends RuntimeException{
    public InadequateNbPlayerException(String msg) {
        super(msg);
    }

    private static final long serialVersionUID = 1L;
}
