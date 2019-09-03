// composition in Java is used for has-a type relationships
// we will make a "Kid" class that has a Mom and a Dad

// our "has a" classes with simple void methods for demonstration
class Mom {
    public void offerHug() {
        System.out.println("Do you want a hug?");
    }
}

class Dad {
    public void dadJoke() {
        System.out.println("Dade joke!");
    }
}

// a Kid class using Composition
class Kid {
    // a Kid "has-a" Mom and Dad
    Mom mom = new Mom();
    Dad dad = new Dad();
}


/***************************| main class |***************************/
public class Composition {
    public static void main(String[] args){
        // a kid will create a Mom and Dad on contruction
        // and they can be used intuitively like mthods
        Kid tommy = new Kid();
        tommy.dad.dadJoke();
        tommy.mom.offerHug();
    }
}
