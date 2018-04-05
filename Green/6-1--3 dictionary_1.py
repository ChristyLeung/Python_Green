# 6-1
favorite_person = {
    'first_name': 'athena',
    'last_name': 'yeung',
    'age': '23',
    'city': 'donguan'
    }
print(favorite_person['first_name'].title())
print(favorite_person['last_name'].title())
print(favorite_person['age'])
print(favorite_person['city'].title())


# 6-2
favorite_numbers = {
    'Christy': '7',
    'Lavande': '18',
    'Season': '18',
    'Saturn': '4',
    'Eric': '8'
    }
print(favorite_numbers)
print("\nChristy's favorite number is " + favorite_numbers['Christy'] + ".\n")
print("\nLavande's favorite number is " + favorite_numbers['Lavande'] + ".\n")
print("\nSeason's favorite number is " + favorite_numbers['Season'] + ".\n")
print("\nSaturn's favorite number is " + favorite_numbers['Saturn'] + ".\n")
print("\nEric's favorite number is " + favorite_numbers['Eric'] + ".\n")


# 6-3
glossaries = {
    'title': 'capitalize the fist letter',
    'upper': 'capitalize all letter',
    'lower': 'lowercase all letter',
    'del': 'del code',
    'append': 'add code at the end of the line'
    }
print(glossaries)
print('\n' + glossaries['title'])
print('\n' + glossaries['upper'])
print('\n' + glossaries['lower'])
print('\n' + glossaries['del'])
print('\n' + glossaries['append'])


for glossary in glossaries.keys():
    if glossary in glossaries.keys():
        print ('\n' + glossary.title() + ":")
for meanning in glossaries.values():
    if meanning in glossaries.values():
        print ('\n' + meanning.title() + ":")
