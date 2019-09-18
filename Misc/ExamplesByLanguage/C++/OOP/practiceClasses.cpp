#include <iostream>
#include <string>

class Character
{
    public:
        int hp;
        std::string name;
        Character(std::string name, int hp)
        {
            this->hp = hp;
            this->name = name;
        }
};

class Wizard : public Character
{
    public:
        std::string wizardName;
        // contructor takes 3 param, 2 of them from Super
        Wizard(std::string name, int hp, std::string wizardName):
            Character(name, hp)
        {
            this->wizardName = wizardName;
        }
};

int main()
{
    Character bjarne{"Bjarne", 15};

    std::cout << std::endl;
    std::cout << "My Character's hp: " << bjarne.hp << std::endl;
    std::cout << "My Character's name: " << bjarne.name << std::endl;

    Wizard dennis{"Dennis",13,"The Grey"};

    std::cout << std::endl;
    std::cout << "My Character's hp: " << dennis.hp << std::endl;
    std::cout << "My Character's name: " << dennis.name << std::endl;
    std::cout << "My Character's wizardName: " << dennis.wizardName << std::endl;

    return 0;
}
