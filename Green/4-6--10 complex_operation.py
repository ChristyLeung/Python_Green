# Try 4-6
odd_numbers = list(range(3,20,2))
print(odd_numbers)

for odd_numbers in range(3,20,2):
    print(odd_numbers)


# Try 4-7
multiple_numbers = list(range(3,30,3))
print(multiple_numbers)

for multiple_numbers in range(3,30,3):
    print(multiple_numbers)


# Try 4-8
cubes = []
for cube in range(1,11):
    cubes.append(cube**3)

print(cubes)


cubes = []
for cube in range(1,11):
    cube = cube**3
    cubes.append(cube)

print(cubes)


# Try 4-9
cubes = [cube**3 for cube in range(1,11)]
print(cubes)
