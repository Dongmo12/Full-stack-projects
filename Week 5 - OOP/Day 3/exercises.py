'''
Exercise 1 : Built-In Functions
Python has many built-in functions, and if you do not know how to use it, you can read document online.
But Python has a built-in document function for every built-in functions.

Write a program to print some Python built-in functions documents, such as abs(), int(), raw_input().
And add documentation for your own function
'''

class Functions:
    '''This is great'''
    def raw_input(self):
        '''This is for raw_input'''

    def absolutes(self):
        '''This for abs operations'''

    def integers(self):
        '''This is for integers'''



obj1 = Functions()
raw_in = obj1.raw_input()
print(Functions.__doc__)

