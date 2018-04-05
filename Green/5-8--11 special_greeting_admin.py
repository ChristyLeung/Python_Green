# Try 5-8
admins = ['admin', 'Christy', 'Yins', 'Mercury', 'Lavande']

for admin in admins:
    if admin == 'admin':
        print("\nHello " + 'admin,' + " would you like to see a status report?\n")
    else:
        print("\nHello " + admin + ".\n")


# Try 5-9
admins = []

if admins:
    for admin in admins:
        print("\nWe need to find some users!\n")
del admins[0:6]
print(admins)


# Try 5-10
current_users = ['admin', 'Christy', 'Yins', 'Mercury', 'Lavande']

new_users = ['admin', 'Christy', 'Yins', 'Hotaru', 'Lavender']

for new_user in new_users:
    if new_user in current_users:
        print("\nPlease enter other user name.\n")
    else:
        print("\nThis user nsame hasn't been used.\n")





# Try 5-11
numbers = ['1', '2', '3', '4', '5', '6', '7', '8','9']
for number in numbers:
    if number == '1':
        print(number + "st")
    elif number == '2':
        print(number + "nd")
    elif number == '3':
        print(number + "rd")
    else:
        print(number + "th")
