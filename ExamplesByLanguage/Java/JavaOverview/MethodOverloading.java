// demonstrate how a method coud be overloaded to give different behavior

/***************************| main class |***************************/
public class MethodOverloading {
    // standard version
    public void sayHi() {
        System.out.println("I am Rando.");
    }
    // overloaded with name option
    public void sayHi(String name){
        System.out.println("Hey " + name + ", I'm Rando.");
    }
    public static void main(String[] args) {
        Rando rando = new Rando();
        // confirm  we've overloaded rando
        rando.sayHi();
        // note they both work and do different things
        rando.sayHi("Bub");
    }
}
