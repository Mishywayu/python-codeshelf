for item in 'Python':
    print(item)

list = ['Python', 'Mosh', 'Sarah']
for i in list:
    print(i)

for y in range(10):
    print(y)

for z in range(5, 10):
    print(z)


# Exercise
# write a program to calculate the total cost of all the items in a shopping cart
prices = [200, 120, 75, 65, 550]
total = 0

for price in prices:
    total = total + price
print(f"The total is Ksh {total}")