# 4.5
# 4.5.1
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


dimensions = (200, 50)
dimensions[0] = 250


# 4.5.2
dimensions = (200, 50)
for dimension in dimensions:
    print(dimensions)


# 4.5.3
dimensions = (200, 50)
print("Original dimensions")
for dimension in dimensions:
    print(dimensions)

dimensions = (400, 100)
print("\nModified dimensions")
for dimension in dimensions:
    print(dimensions)
