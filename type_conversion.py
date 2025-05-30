birth_year = input("Birth year: ")
print(type(birth_year))
age = 2025 - int(birth_year)
print(type(age))
print(age)


# Exercise
"""
Ask a user their weight (in pounds), convert it
to kilograms and print on the terminal.
"""
# 1 kg = 2.20462 pounds
user_weight = input("How many pounds do you weigh? ")
print(type(user_weight))
weight_in_Kg = int(user_weight) / 2.20462
print(type(weight_in_Kg))
user_kg = str(weight_in_Kg)
print(type(user_kg))
print("This user weighs " + user_kg + " Kgs")