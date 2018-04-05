# 6-4
glossaries = {
    'title': 'capitalize the fist letter',
    'upper': 'capitalize all letter',
    'lower': 'lowercase all letter',
    'del': 'del code',
    'append': 'add code at the end of the line',
    'insert': 'add code at any place',
    'pop': 'delete code at ant place',
    'sort': 'sort code by letter a-z',
    'reverse': 'reverse the order of code',
    'keys': 'run through the code lines'
    }

for name in glossaries.keys():
    print(name)



# 6-5
rivers = {
    'nile': 'egypt',
    'times': 'united kindom',
    'yangtze': 'china'
    }
for river, country in rivers.items():
    print("\nThe " + river.title() +
        " runs through " + country.title() + ".\n")

for river in rivers:
    print(river.title() + '\n')

for country in rivers.values():
    print(country.title() + '\n')


# 6-6
investigations = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(investigations.keys()):

    if name in investigations.keys():
        print('\n' + name.title() + ", thank you for your cooperation!")
if 'paul' not in investigations:
    print("\nPaul, we would like to invite you to join our investigation.")
