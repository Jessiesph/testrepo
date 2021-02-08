
# conditions
'''
if it's hot
    It's a hot day
    Drink plenty of water
otherwise if it's cold'
    It's a cold day' \
    Wear warm clothes
otherwise
    It's a lovely day


is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Ware warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")
'''
# Exercise: price of a house is 1$M. if buyer has good credit, they need to put down 10%, otherwise, they need 20%

price = 1000000
good_credit = False
if good_credit:
    down_payment = price * 0.1
    print(f"Your down payment is ${down_payment}")
else:
    down_payment = price * 0.2
    print(f"Your down payment is ${down_payment}")
print("For the house purchase")


