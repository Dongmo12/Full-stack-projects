'''
class Foods():
    """
    docstring
    """
    def __init__(self, name='', weight=12):
        print("Hello world!!")
        self.name = 'cococho'
        self.weight = 10


    def printings(self):
        print("the name is {} and your weight is {}".format(self.name, self.weight))


food1 = Foods()
food1.printings()

'''

'''
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

## create an instance of the class
p = Point(3,4)

## access the attributes
print("p.x is:", p.x)
print("p.y is:", p.y)
'''
''' 
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
'''
class Computer():

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        #Analyse the line below
        print(self)

# computer1 = Computer()
# computer1.brand = "Apple"
# print(computer1.brand)

computer2 = Computer()

Computer.description(computer2, "Mark")
# IS THE SAME AS:
computer2.description("Mark wirberg")