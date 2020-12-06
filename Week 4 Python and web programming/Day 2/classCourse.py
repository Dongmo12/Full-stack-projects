'''
 Given this list: list1 = [5, 10, 15, 20, 25, 50, 20], find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

Hint : Look at the index method


list1 = [5, 10, 15, 20, 25, 50, 20]

x = list1[list1.index(20)]
list1[x]=200

print(list1)
'''

num = int(input("Please enter a number: "))

print("1*{}=".format(1*num))
print("2*{}=".format(2*num))
print("3*{}=".format(3*num))
print("4*{}=".format(4*num))
print("5*{}=".format(5*num))
print("6*{}=".format(6*num))
print("7*{}=".format(7*num))
print("8*{}=".format(8*num))
print("9*{}=".format(9*num))
print("10*{}=".format(10*num))
print("11*{}=".format(11*num))
print("12*{}=".format(12*num))


for i in range(0,12):
    print("{}*{}={}".format(i,num,i * num))