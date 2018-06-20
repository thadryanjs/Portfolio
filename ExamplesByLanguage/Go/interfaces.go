package main

import "fmt"
import "reflect"

/* how and why to use interfaces in Go*/

// Hero structure and functions 
type Hero struct {
    Person
}

func(h Hero) Speak() string {
    return "I am a hero!"
}



// Villian structure and functions 
type Villian struct {
    Person
}

func(v Villian) Speak() string {
    return "I am a villian"
}



// Define a Speaker interface for broad use with Talk
type Speaker interface {
    Speak() string
}

// define talk function for Speakers
func Talk(s Speaker) {
    fmt.Println(reflect.TypeOf(s).Name(), "says:", s.Speak())
}


// le main
func main() {

    // make strctures
    h := Hero{name: "Galavant"}
    v := Villian{name: "Lasseter"}

    // test on structs - will make tem each do their respective versions 
    Talk(h)
    Talk(v)
}
