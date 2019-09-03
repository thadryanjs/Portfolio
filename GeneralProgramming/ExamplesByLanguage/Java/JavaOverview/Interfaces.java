// interface Dancer features twist() and shout() methods
interface Dancer {
    public void twist();
    public void shout();
}
// an example dancer - note he has his way of twisting and shouting
class Tommy implements Dancer {
    // define how Tommy specifically twists and shouts
    public void twist() {
        System.out.println("~ How Tommy twists!");
    }
    public void shout() {
        System.out.println("~ How Tommy shouts!");
    }
}
// A different dancer with different implementation of the same methods
class Suzie implements Dancer {
    // define how Suzie specifically twists and shouts
    public void twist() {
        System.out.println("How Suzie twists! ~");
    }
    public void shout() {
        System.out.println("How Suzie shouts! ~");
    }
}

/***************************| main class |***************************/
public class Interfaces {
    // we will now write a method that takes a list of ANY dancers
    // this will allow us to call and method in the interface and know
    // they will each do it in their own way without having to specify
    static void TwistAndShout(Dancer[] dancers) {
        for(Dancer d : dancers) {
                // call the generic interface methods
                d.twist();
                d.shout();
        }
    }
    /***************| main|*****************/
    public static void main(String[] args) {
        // a list of dancers
        Dancer[] dancers = {
            new Tommy(),
            new Suzie(),
        };
        // they do their own version of twist() and shout()
        TwistAndShout(dancers);
    }
}
