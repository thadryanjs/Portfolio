# Perl 1
print "Hello Perl\n";


# Perl 2
print "Hello ";

print "World\n";

# Perl 3
my $name = "Larry\n";

print $name;


# Perl 4
use strict;
use warnings;

#declare name

my $name = "Larry";

#find the length with the length() function

print length($name), "\n";

#print upper and lower case using keywords

print uc $name, "\n";

print lc $name, "\n";

#split the word so we can print each character

foreach my $character (split(//, $name)) {
    
    print $character, "\n";
}

# Perl 5
use strict;
use warnings;

my $name = "Larry";

foreach my $character (split(//, $name))
{
    print $character, "\n";
    
    print "Still Going, \n";
}

# Pel 6
use strict;
use warnings;

my $name = "Larry";

foreach my $character (split(//, $name))
{
 
 print $character, "\n";

}
print "Not Still Going"

# Perl 7
use strict;
use warnings;

my $number = 10;

if ( $number > 10 ) {
    print "The number is over ten";
} else { 
    if ( $number < 10 ) {
        print "The number is less than ten";
} else {
    print "The number is ten\n";
    }
}

# Perl 8
my %residues = ( "A"=>  89.000,  "R"=> 174.000, "N"=> 132.000, "D"=> 133.000, "C"=> 121.000, 
                 "Q"=>  146.000, "E"=> 147.000, "G"=> 75.000,  "H"=> 155.000, "I"=> 131.000,
                 "L"=>  131.000, "K"=> 146.000, "M"=> 149.000, "F"=> 165.000, "P"=> 115.000, 
                 "S"=>  105.000, "T"=> 119.000, "W"=> 204.000, "Y"=> 181.000, "V"=> 117.000 );


# Perl 9
use strict;
use warnings;

sub addOne {
        my $x = $_[0]; #capture the first element of the argument array as a scalar
        return $x+1
}

print addOne(10), "\n";
