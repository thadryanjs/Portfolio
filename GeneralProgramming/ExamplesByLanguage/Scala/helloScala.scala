import scala.collection.mutable.ArrayBuffer                    // needed for dynamic arrays


/* classes and traits */                                                                                                                              case class static_point(x: Int, y: Int)                         // case classes are used for small, immutable values.
                                                                // Set to unchangable automatically. Super neat! 
                                                                
class dynamicPoint(var x: Int, var y: Int)                      // a small, more typical class
            						        // var means they can change, val means they can't

/*                                               \
   this class allows the user to pass a starting 
   value that can then only be manipulated from 
   within the object w getter/setter denoted by
\  the pre or post "_".                         */

class pointWithGetSet(val xIn: Int) {
  private var _x = xIn                                          // sets x to value of xIn
  def x = _x                                                    // getter
  def x_= (newX: Int) = _x = newX                               // set x to value of newX
}
  

trait lover {                                                   // implementing traits is straightforward
  def love(): Unit = {                                          // Unit means Void
    println("I am a lover!")
  }
}
  
trait fighter {
  def fight(): Unit = {
    println("I am a fighter!")
  }
}
  
class rouge(name: String) extends lover with fighter {          // extend a class with traits
  def enGarde(): Unit = {
    love
    fight
    println("I am " + name + "!")
  }
}                                                               // overriding is easy - revengeSeeker will 
                                                                // have his own version of enGard  
class revengeSeeker(name: String, warning: String) extends rouge(name) {
  override def enGarde(): Unit = {                                        
    love 
    fight
    println("I am " + name + " " + warning)
  }
}

/*---------------------------| ~ main ~ |------------------------------\

 the class containing main is the name of the program like in Java. 
 main is contained within a singleton object, takes array of strings,
 is void (returns Unit).
\---------------------------------------------------------------------*/
   
object helloScala {
  def main(args: Array[String]): Unit = {                       // the main starts the program i

    println("/* strings, print, format */")
    val greeting1 = "Hello from Scala. I have type inference."  // declaring a string 
    val greeting2: String = " You can also declare explicitly."
    println(greeting1 + greeting2)
    
    val word = "word"                                           // strings have a foreach method
    word.foreach { letter =>                                    // that splits the string  
      println(s"The letter is: $letter")                        // interpolate strings (Scala 2.1 +)
    }

    for( i <- 0 until word.length) {                            // "until" subtracts 1 from range to avoid 
      println("I have options!")                                // so you don't index errors counting from 0
    }

    val otherWord = "bird"                                      // indices iterates by index to compare
    for(i <- word.indices) {                                    // like a tradition C-style for loop 
      println(word(i) + " " + otherWord(i))
    }
    
    val height: Double = 1.5                                   
    println(f"height: $height%.5f")                             // format with f interpolated as printf style tags
    
    println("/* arrays + ArrayBuffers*/")
    val numbers = Array(2,4,6,8,10)                             // arrays are initialized with type inference 
    println(numbers(4))
    numbers.foreach { number =>                                 // arrays have a foreach method
      println(number)
    }
    
    println("/* ranges */")
    println("A range, 1 to 3")
    for(number <- 1 to 3 ) {                                    // ranges use english-like syntax 
      println(number)
    }

    val dynamicArray = ArrayBuffer[Int]()                       // dynamic array, empty
    numbers.foreach{ number =>                       
      dynamicArray += number                                    // add all number in other array
    }
    dynamicArray += 12                                          // add another - contains 2,4,6,8,10,12

    println(dynamicArray)


    println("/* map (transformation) *")
    val doublednumbers = (1 to 5).map { num => num * 2 }        // map can act on ranges
    println("The last nummber is now " + doublednumbers(4))
    
    
    println("/* functions */")
    var addOne = (x: Int) => x + 1                              // a simple function acting on x, yields x+1
    println(addOne(99))
    
    def sayBand (bandName: String = "Pinegrove"): Unit = {      // easy python style defaults - no overloading needed!
      println(bandName)
    }
    sayBand()                                                   // nothing passed, default activates
    
    
    println("/* Map (data structure */")
    var stars = Map("Lee" -> "Pace", "Kerry" -> "Bishe'",       // paired data is stored with Map 
                                  "MaKenzie" -> "Davis")
    
    stars += ("Scoot" -> "McNairy")                             // add new entries 
    stars += ("Toby"  -> "Huss")
    stars.keys.foreach{ actor =>                                // maps also use foreach 
      println(actor + " " + stars(actor))                       // can be declared empty, in advance: 
    }                                                           //     var stars : Map[String, String] = Map()
    
    var reversedStars = for((k, v) <- stars) yield (v, k)       // reverse by iterating and yield

    for ((k,v) <- reversedStars) println(k + " " + v)           // print k,v one liner 

    println("/* using classes and methods */")
    val staticLocation1 = new static_point(x = 1, y = 2)        // a new instance of static point class    
    println(staticLocation1)
    
    val staticLocation2 = new static_point(x = 1, y = 3)        // classes/control flow  - compare classes directly 
    
    /* ...and conditionals */
    if(staticLocation1 == staticLocation2) {
      println("Points are in the same spot")
    }
    else{
      println("Points are not in the same spot") 
    }
    
    val dynamicLocation = new dynamicPoint (x = 1, y = 1)      // create mutable point. x will change
    dynamicLocation.x = 5                                      // change x 
    println("Dynamic: "+ dynamicLocation.x + " " + dynamicLocation.y)
     
    var getSet = new pointWithGetSet(xIn = 20)                 // class will allow change from within the object
    getSet.x = 30                                              // will be printed as 30 due to auto setter
    println("Value was 20, is now: " + getSet.x)
    
    val zoro = new rouge("Zoro")                               // make a new rouge
    zoro.enGarde                                               // put foes on notice!
                                                               // will use overriden enGarde
    val inigo = new revengeSeeker(name = "Inigo Montoya", warning = "Prepare to die!")
    inigo.enGarde  
  }  
}
