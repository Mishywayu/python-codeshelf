"""
if temperature is greater than 30, it's a hot day
otherwise if it's less than 10, it's cold day
otherwise, it's neither hot nor cold
"""

temperature = 20

if temperature > 30:
    print("It's a hot day")
elif temperature < 10:
    print("It's a cold day")
else:
    print("It's neither hot nor cold")


# Exercise
"""
if name is less han 3 characters long, name must be atleast 3 characters
otherwise if it's more than 50 characters long, name can be a maximum of 50 characters
otherwise, name looks good!
"""
name = input("Input your name: ")

if len(name) < 3:
    print("Name must be atleast 3 characters.")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")