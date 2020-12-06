'''
Exercise 1 : Favorite Numbers
Create a set called my_fav_numbers with your favorites numbers.
Add two new numbers to it.
Remove the last one.
Create a set called friend_fav_numbers with your friend’s favorites numbers.
Concatenate my_fav_numbers and friend_fav_numbers to our_fav_numbers.

# Solution

my_fav_numbers = {12,16,20}
print(my_fav_numbers)
my_fav_numbers.add(30)
print(my_fav_numbers)
my_fav_numbers.add(15)
print(my_fav_numbers)
my_fav_numbers.pop()
print(my_fav_numbers)
my_fav_numbers.pop()
print(my_fav_numbers)


friend_fav_numbers = {"jeff","jose","Armand"}


our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)
'''


'''
Exercise 2: Tuple
Given a tuple with integers is it possible to add more integers to the tuple?


Answer: It would not be possible to add because a tuple is a collection which is ordered and unchangeable.

'''

'''
 Use a for loop to print the numbers from 1 to 20, inclusive.

# Solution
for num in range(1,21):
    print(num)
'''


'''
Exercise 4: Floats
Recap – What is a float? What is the difference between an integer and a float?
Can you think of another way of generating a sequence of floats?
Create a list containing the sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 without hard-coding the sequence.

#Solution

float represent real numbers and are written with a decimal point dividing the integer and fractional parts.

An integer (more commonly called an int) is a number without a decimal point. A float is a floating-point number, which means it is a number that has a decimal place. Floats are used when more precision is needed.

'''

list = list(range(1,6) )
for x in list:
    print(x)
    x = x+0.5
    print(x)