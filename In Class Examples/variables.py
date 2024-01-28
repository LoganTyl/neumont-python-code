a = 3
b = 4
print(a+b)

x = a
a = 5
print(x)

c = 3.14
d = a + c
e = d - a
print(c, d, e)

a=True
print(a)
a="Bob"

my_string="ABCDEFGHIJKLM"
print(my_string)
print(len(my_string))
print(my_string[3])

print(my_string[5:10])  #goes from indexes 5 to 9; 10 is exclusive
print(my_string[2:])
print(my_string[:3])
print(my_string[:-3])

print(my_string[::2])  #goes every other index
print(my_string[3:9:2])

print(my_string[::-1])  #reverses string

my_string = my_string * 2
print(my_string)
print()

greeting = "Howdy"
name="Bob"

print(greeting + ", " + name + "!")
print(f"{greeting}, {name}!")
print("{0}, {1}!".format(greeting, name))
print("{greeting}, {name}!".format(greeting=greeting, name=name))
print("%s, my name is %s." %("Hiya", "Harry"))
print("Hello, my name is %s and I am %i years old." %("Jim", 34))

print("Hello, my name is %s and I am %.2f years old." %("Jim", 34))
print("Hello, my name is %s and I am %.10f years old." %("Jim", 34))
print("Hello, my name is %s and I am %.20f years old." %("Jim", 34))
print()

email = """
Date: {date}

Dear {name},

I look forward to seeing you later on the hill.

Sincerely,
{my_name}
"""

import datetime
todaysDate = datetime.date.today()
# print(todaysDate)
the_date = "{today.month}/{today.day}/{today.year}".format(today=todaysDate)
# print(the_date)
print(email.format(date=the_date, name="Jill", my_name="Jack"))
print()

num1 = input("Enter the first number => ")
num2 = input('Enter the second number => ')
num3 = int(num1) + int(num2)
print(f"{num1} + {num2} = {num3}")

