use strict;
use warnings;

# get say fcn
use feature "say";

# declare class "Person"
package Person
{
    # imports Moose
    use Moose;

    # = 'const string name' in normal OO language. Read only string
    has "name", is => "ro", isa => "Str";

    # define a method to say hello
    sub sayHello
    {
        my $self = shift;       # explicit binding (self.method in Python)
        say "Hello!";           # like Ruby's 'puts'
    }

    # define a method to say Person's name
    sub sayName
    {
        my $self = shift;
        say $self -> name;      # access self's name attribiute
    }

    # define a method to print a greeting with text and name attribute
    sub introduction
    {
        my $self = shift;
        say "Hello, my name is ", $self -> name, ".";
    }
}

# initialize new Person named "Gandalf"
my $hero = Person -> new( name => "Gandalf");

# have $hero say "Hello!"
$hero -> sayHello;

# have $hero say his name
$hero -> sayName;

# have hero introduce himself
$hero -> introduction;
