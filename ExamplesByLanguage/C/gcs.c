#include <stdio.h>
#include <string.h>

// define array length macro - no. entries / their size
#define ARRAY_LENGTH(array) ( sizeof(array)/sizeof(array[0]) )

// define and append function - adds character to end
// of char array passed as a pointer
void append(char* string, char character)
{
    // find length, add character at that index, add null term.
    int len = strlen(string);
    string[len] = character;
    string[len + 1] = '\0';
}

// define a function that counts the number of
// non '\0' in a character array
int charCount(char* x)
{
    // iterate and count real chars
    int characters = 0;

    while (*x != '\0')
    {
        characters++;
        x++;
    }
    return characters;
}

int main()
{
    // test strings that don't start on match
    char string1[] = "THADRYAN";
    char string2[] = "XXXXRYAN";

    // char arrays up to maximum length of string
    char current[ARRAY_LENGTH(string1)+1] = {'\0'};
    char longest[ARRAY_LENGTH(string1)+1] = {'\0'};

    /* the "current" iter needs it's own counter in case the first
       letter is not a hit or else it will pass a point to the append
       function that isn't its start (if you use the i declared in the
       for loop. Skipping this results in a function that only works if
       a match starts onthe first character                           */
    int currentIter = 0;

    // iterate through the arrays, compare chars
    for ( int i = 0; i <= ARRAY_LENGTH(string1); i++ )
    {
        if ( string1[i] == string2[i] )
        {
            // if they match declare pointer, pass to append,
            // then increment the currentIter counter
            char* ptrCurrent = &current[currentIter];
            append(ptrCurrent, string1[i]);
            currentIter++;
        } else {
            continue;
        }

        // copy "current" to "longest" var if it's largest yet
        if ( charCount(current) > charCount(longest)) {
            memcpy(longest, current, sizeof(current));
        }
    }
    printf(longest);
    printf("\n");
return 0;
}
