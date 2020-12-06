'''
Exercise 4 : Your Computer Brand
Create a variable called computer_brand that contains the brand of your computer.
Insert and print the above variable in a sentence,like "I have a razer computer".

# Solution
computer_brand = "msi"
print('I have a {} computer'.format(computer_brand))
'''

'''
Exercise 5: Your Information
Create a variable called name, and give it your name as a value (text)
Create a variable called age, and give it your age as a value (number)
Create a variable called shoe_size, and give it your shoe size as a value
Create a variable called info. Its value should be an interesting sentence about yourself, including your name, age, and shoe size. Use the variables you created earlier.
Have your code print the info message.
Run your code

#Solution
name = "jeff"
age = 32
shoe_size = 40
info = "My name is {} and I am {} year old. My shoe size is {}. I can't change so just accept me as I am."
print(info.format(name,age,shoe_size))
'''

'''
Exercise 6: Odd Or Even
Write a script that asks the user for a number and determines whether this number is odd or even

#solution


val = int(input('Please, enter your name: '))

if val%2==0:
    print('{} is even'.format(val))
else:
    print('{} is odd'.format(val))

'''


'''
Exercise 7 : What’s Your Name ?
Write a script that asks the user for his name and determines
whether or not you have the same name, print out a funny message based on the outcome

#Solution


myName = 'Alexandra'.lower()
userName = input("Please, enter your name:").lower()

if userName==myName:
    print('{} we have the same name.'.format(userName))
else:
    print('{} sorry but we don t have the same name.'.format(userName))
'''

'''
Exercise 8 : Tall Enough To Ride A Roller Coaster
Write a script that will ask the user for their height in inches, print a message if they can ride a roller
coaster or not based on if they are taller than 145cm
Please note that the input is in inches and you’re calculating vs cm,
you’ll need to convert your data accordingly
# Solution


inches = int(input("Please enter your height in inches: "))
convert = int(inches*2.54)
val = 145

if convert>val:
    print("You entered {} and you are {} cm so you can ride a roller coaster".format(inches, convert))
else:
    print("You entered {} and you are {} cm so you can't ride a roller coaster".format(inches, convert))
'''