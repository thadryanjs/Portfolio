import shapes.Circle;
import shapes.Square;
import shapes.Invisible;
import java.util.*;

public class main
{
    public static void main(String[] args)
    {
        // testing the Circle
        Circle c = new Circle();
        c.hello();

        // testing the Square
        Square s = new Square();
        s.hello();

        // no declaration! (static)
        Invisible.hello();
    }
}
