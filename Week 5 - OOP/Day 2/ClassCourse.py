'''
Exercise On Inheritance And Composition: Door Class
Try to recreate the class explained below:
We have a class called `Door` that has an attribute of `is_opened` declared when an instance is initiated.
We can create a class called `BlockedDoor` that inherits from the base class `Door`.
We just override the parent class's functions of `open_door()` and `close_door()`
with our own `BlockedDoor` version of those functions,
which simply raises an Error that a blocked door cannot be opened or closed.
'''

# To be done



#
# class Computer():
#
#     def __init__(self):
#         self.name = "Apple Computer" # public
#         self.__max_price = 900 # private
#
#     def sell(self):            # public method
#         print("Selling Price: {}".format(self.__max_price))
#
#     def __sell(self):          # private method
#       print('This is private method')
#
#     def set_max_price(self, price):
#         self.__max_price = price
#
# c = Computer()
# c.sell()
# # >> Selling Price: 900
# c.__sell()
# class Book():
#     def __init__(self, title, author, publication_date, price):
#         self.title = title
#         self.author = author
#         self.publication = publication_date
#         self.price = price
#
#     def present(self):
#         print(f'Title: {self.title}')
#
# class Fiction(Book):
#     def __init__(self, title, author, publication_date, price, is_awesome):
#         super().__init__(title, author, publication_date, price)
#         self.genre = 'Fiction'
#         self.is_awesome = is_awesome
#         if self.is_awesome:
#             self.bored = False
#             print('Woow this is an awesome book')
#         else:
#             self.bored = True
#             print('I am very bored')
#
# if __name__ == '__main__':
#     foundation = Fiction('Asimov', 'Foundation', '1966', '5£', True)
#     foundation.present()
#     print(foundation.price)
#     print(foundation.bored)
#     boring_book = Fiction('boring_guy', 'boring_title', 'boring_date', '9000£', False)
#     print(boring_book.bored)

# def age():
#     user_age = input("How old are you?\n>>> ")
#     #######
#     try:
#         user_age = int(user_age)
#         print("I AM AFTER USER_AGE")
#     except:
#         print("Your age is not a real age")
#         user_age = 0
#     #######
#     print("Next year, you will be {} years old".format(user_age+1))
#
# age()
#
# valid_flag = False
# while not valid_flag:
#     userage = input("How old are you?")
#     try:
#         userage = int(userage)
#         valid_flag = True
#     except:
#         print("Please enter a real age")
#
# print("Next year, your age will be",userage+1)

#import pizza
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')