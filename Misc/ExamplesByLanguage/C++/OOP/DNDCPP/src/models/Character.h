#include <iostream>
#include <string>
#include "enum_playableClass.h"

class Character
{
    public:
        std::string name;
    private:
        int maxHp;
        int currentHp;
    protected:
        enum playableClass characterClass;

    public:
        Character(std::string name, enum playableClass classIn)
        {
            this->name = name;
            this->characterClass = classIn;
        }

        void describeSelf()
        {
            std::cout << "\t Chacter Description \t" << std::endl;
            std::cout << "name: " << this->name << std::endl;
            std::cout << "class: " << this->characterClass << std::endl;
        }
};
