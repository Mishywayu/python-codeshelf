# IF statements
# if day = "hot":
#     print("It's a hot day, drink plenty of water")
# elif day = "cold":
#     print("It's a cold day, wear warm clothes")
# else:
#     print("It's a lovely day")

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")


# Exercise
"""
Price of a house is $1M.
if buyer has good credit, they need to put down 10%
otherwise, they need to put down 20%
Print the down payment
"""
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f"down payment: ${down_payment}")