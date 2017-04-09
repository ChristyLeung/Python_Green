# Try 5-2
car = 'subaru'
if car == 'subaru':
    print("\nThat is correct. Congratularions!")
if car != 'audi':
    print("\nThat is not the correct answer. Please try again!")


car = 'toyota'
if car == 'toyota':
    print("\nThat is correct. Congratularions!")
if car != 'subaru':
    print("\nThat is not the correct answer. Please try again!")


car = 'BMW'
car == 'bmw'
print("\nFalse")

car = 'bmw'
car.lower() == 'bmw'
print("\nTrue")

car = 'benz'
car.lower() == 'benz'
print("\nTrue")


number_1 = 18
number_1 == 18

number_1 = 18
if number_1 != 26:
    print("\nThat is not the correct answer. Please try again!")

number_1 = 18
number_2 = 26
number_2 > 18
number_1 < 26
number_2 >= 18
number_1 <= 26


cars = ['cadillac', 'subaru', 'BMW', 'Benz', 'toyota']
car = 'cadillac'

if car in cars:
    print('\n' + car.title() + ", you are right!")

car = 'audi'

if car not in cars:
    print('\n' + car.title() + ", you are wrong. Please try again!")
