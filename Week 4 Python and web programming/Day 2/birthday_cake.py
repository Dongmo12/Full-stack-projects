birthday = input("please enter your birthday date DD/MM/YYYY: ")
bd_array= birthday.split("/")
bd_year = bd_array[2]
age = 2020 - int(bd_year)
age_string = str(age)
last_digit = int(age_string[1])

print(last_digit)

cake = ('''
    ___{'i'*last_digit}___
          |:H:a:p:p:y:|
        __|___________|__
       |^^^^^^^^^^^^^^^^^|
       |:B:i:r:t:h:d:a:y:|
       |                 |
       ~~~~~~~~~~~~~~~~~~~
    
    ''')

print(cake)