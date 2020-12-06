'''
Exercise 1 : Pets
Consider this code

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


Add another cat breed
Create a list of all of the pets (create 3 cat instances from the above) my_cats = []
Instantiate the Pet class with all your cats. Use the variable my_pets
Output all of the cats walking using the my_pets instance


# Solution
class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Burmese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

obj1 = Bengal('Bengal', 12)
obj2 = Chartreux('Chartreux', 15)
obj3 = Burmese('Burmese', 11)
my_cats = []
my_cats.append(obj1)
my_cats.append(obj2)
my_cats.append(obj3)

my_pets = Pets(my_cats)
my_pets.walk()

'''

'''
Exercise 2 : Dogs
Create a class named Dog with the attributes name, age, weight
Implement the following methods for the class:
bark: returns a string of “ barks”.
run_speed: returns the dogs running speed (weight/age *10).
fight : gets parameter of other_dog, returns string of which dog won the fight between them, 
whichever has a higher run_speedweight* should win.
Create 3 dogs and use some of your methods
'''


class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def Barks(self):
        print("Barking")

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if self.run_speed() > other_dog.run_speed():
            print(f"{self.name} is the winner")
        else:
            print(f'{other_dog.name} is the winner')



dog1 = Dog('Rex', 11, 10)
dog2 = Dog('Alex', 12, 30)
dog3 = Dog('Vexus', 13, 50)

dog1.run_speed()
dog2.run_speed()
dog3.run_speed()
dog3.fight(dog2)

