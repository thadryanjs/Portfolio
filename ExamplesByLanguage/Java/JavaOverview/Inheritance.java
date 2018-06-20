/* simple Inheritance */

// simple class
class CivilServant {
    String name;
}

// make a class that extends it
class Firefighter extends CivilServant {
    String homeRig;
}

/***************************| main class |***************************/
public class Inheritance {
    public static void main(String[] args) {
        // make an instance of the simple class
        CivilServant randomMailMan = new CivilServant();
        randomMailMan.name = "Bo";
        System.out.println(randomMailMan.name);

        // make an instance of the complex one
        // notice that it has both fields
        Firefighter thadryan = new Firefighter();
        thadryan.name = "Thadryan";
        thadryan.homeRig = "Ladder 1";
        System.out.println(thadryan.name);
        System.out.println(thadryan.homeRig);
    }

}
