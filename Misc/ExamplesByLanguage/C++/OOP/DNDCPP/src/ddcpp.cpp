#include <iostream>
#include <string>
#include "Fighter.h"

int main()
{
    std::cout << "Main online" << std::endl;

    Character testChar {"Thadryan!", MAGICUSER};
    std::cout << testChar.name << std::endl;
    testChar.describeSelf();

    Fighter testFighter {"Thadrion", FIGHTER, "TIGER!"};
    testFighter.fightingStyle = "Lotus";

    std::cout << "Hello" << std::endl;
    std::cout << testFighter.fightingStyle << std::endl;
    return 0;
}
