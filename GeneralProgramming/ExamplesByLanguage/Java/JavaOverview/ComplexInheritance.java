// inheritance using the contructor

// create an example base class with contructor
class CivilServantGuy {
    String name;
    // contructor takes name input
    CivilServantGuy(String nameIn) {
        this.name = nameIn;
    }
}

// extends the class and use its contructor
class FirefighterGuy extends CivilServantGuy {
    // contructor with specials super syntax
    FirefighterGuy(String nameIn){
        super(nameIn);
    }
}

// modified contructor adds new values and then uses normal syntax
class FirefighterGuy2 extends CivilServantGuy {
    // new value
    String rank;
    FirefighterGuy2(String nameIn, String rankIn) {
        // take the other contructor elements
        super(nameIn);
        // and add our own
        this.rank = rankIn;
    }
}
/***************************| main class |***************************/
public class ComplexInheritance {
    public static void main(String[] args) {
        // examine the base class
        CivilServantGuy freddie = new CivilServantGuy("Freddie");
        // simple inheritance of the contructor
        FirefighterGuy mike = new FirefighterGuy("Mike");
        // modification of the constructor to take two args
        FirefighterGuy2 mitch = new FirefighterGuy2("Mitch", "Lt.");

        // mike and freddie use the default contructor...
        System.out.println(freddie.name);
        System.out.println(mike.name);
        // ... mitch does, too, but augments it
        System.out.println(mitch.name);
        System.out.println(mitch.rank);
    }
}
