# Exercise
# My Solution
Lbs = 2.20462

weight = input("Weight: ")
user_weight = int(weight)
question = input("(L)bs or (K)g: ")

if 'L' or 'l' in question:
    new_weight = user_weight / Lbs
    print(f"You are {new_weight} pounds")
elif 'K' or 'k' in question:
    new_weight = user_weight * Lbs
    print(f"You are {new_weight} Kgs")
else:
    print("Please specify if it's (L)bs or (K)g.")


# Mosh's Solution
