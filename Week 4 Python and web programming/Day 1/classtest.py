print("Hello welcome to the program!!")
print("Please, enter a number:")

for x in range(100):
    if x%3==0:
        print("Fizz")
    elif x%5==0:
        print("Buzz")
    elif (x%3==0) and  (x%5==0):
        print("FizzBuzz")
    else:
        print("Nothing to say")