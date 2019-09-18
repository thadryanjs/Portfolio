#include <iostream>
#include <string>
#include "Character.h"

class Fighter : Character
{
    public:
        std::string fightingStyle;
        Fighter(std::string name, enum playableClass classIn,std::string fightingStyleIn)
        : Character(name, classIn)
        {
            this->fightingStyle = fightingStyleIn;
        }

};
