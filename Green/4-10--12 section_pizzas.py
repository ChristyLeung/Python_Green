# Try 4-10
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("The first three items in the list are:")
print(players[:3])


players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Three items from the middle of the list are:")
print(players[1:4])


players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("The last three items in the list are:")
print(players[2:])


# Try4-11
pizzas = ['cheese', 'durian', 'pepperoni', 'new orleans']
friend_pizzas = ['cheese', 'durian', 'pepperoni', 'shrimp']

for pizza in pizzas:
    print("My favorite pizzas are:")
    print(pizzas)

for friend_pizza in friend_pizzas:
    print("\nMy friend's favorite pizzas are:")
    print(friend_pizzas)


# Try4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

for my_food in my_foods:
    print("My favorite foods are:")
    print(my_foods)

for friend_food in friend_foods:
    print("\nMy friend's favorite foods are:")
    print(friend_foods)
