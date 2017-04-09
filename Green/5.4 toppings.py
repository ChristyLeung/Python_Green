# 5.4
# 5.4.1
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!\n")


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!\n")


# 5.4.2
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
         print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!\n")
else:
    print("\nAre you sure you want a plain pizza?\n")


# 5.4.3
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("\nAdding " + requested_topping + ".\n")
    else:
        print("\nSorry, we don't have " + requested_topping + ".\n")
print("\nFinished making your pizza!\n")
