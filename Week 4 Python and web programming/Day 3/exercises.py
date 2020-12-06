'''
Exercise 1 : Convert Lists Into Dictionaries
Convert the two following lists, into dictionaries.
Hint: Use the zip method
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Expected output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# Solution
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
x=zip(keys,values)
print(tuple(x))
'''

'''
Exercise 2 : Cinemax #2
“Continuation of Exercise Cinemax of Week4Day2 XP”

A movie theater charges different ticket prices depending on a person’s age.
if a person is under the age of 3, the ticket is free
if they are between 3 and 12, the ticket is $10;
and if they are over age 12, the ticket is $15 .
Here is the object you will work with : family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
Using a for loop, the dictionary above, and the instructions, print out how much each family member will need to pay alongside their name
After the loop print out the family’s total cost for the movies
Bonus: let the user input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty)
*************************************************************************

Exercise 12: Cinemax
A movie theater charges different ticket prices depending on a person’s age.
if a person is under the age of 3, the ticket is free
if they are between 3 and 12, the ticket is $10;
and if they are over age 12, the ticket is $15 .
Apply it to a family, ask the user what the age of each of the people that want a ticket is.
Store the total cost of all the tickets for this group and print it out.
A group of teenagers is coming to your movie theater and want to see a movie that is restricted for people between 16 and 21 years old.
Write a program that ask every user their age, and then tell them which one can see the movie.
Tip: Try to add the allowed ones to a list.
'''

famNum = int( input("You family has how many person? "))
x=1
#while x<=famNum:
for x in range(famNum):
    age = int(input("Please, enter your age: "))
    if age<3:
        print("The ticket is free for you since you are {} year old".format(age))
    elif age>3 and age<12:
        print("The ticket is $10 for you since you are {} year old".format(age))
    elif age>12:
        print("The ticket is $15 for you since you are {} year old".format(age))
#    x+=1