# 6-7
people = {
    'ayeung': {
        'first_name': 'athena',
        'last_name': 'yeung',
        'age': '23',
        'city': 'donguan',
        },

    'jwong': {
        'first_name': 'jaye',
        'last_name': 'wong',
        'age': '23',
        'city': 'england',
        },

    'cleung': {
        'first_name': 'christy',
        'last_name': 'leung',
        'age': '23',
        'city': 'guangzhou',
        },

    }

for person, person_info in people.items():
    print("\nName: " + person)
    full_name = person_info['first_name'] + " " + person_info['last_name']
    age = person_info['age']
    location = person_info['city']

    print("\tFull name: " + full_name.title())
    print("\tAge: " + age)
    print("\tLocation: " + location.title())


# 6-8
pets = {
    'hedwig': {
        'type': 'owl',
        'owner': 'harry potter',
        },

    'crookshanks': {
        'type': 'cat',
        'owner': 'hermione granger',
        },

     'scabbers': {
         'type': 'rat',
         'owner': 'ron weasley',
        },

    }

for pet, pet_info in pets.items():
    print("\nPet: " + pet.title())
    types = pet_info['type']
    owner = pet_info['owner']

    print("\tOwner name: " + owner.title())
    print("\tType: " + types)


# 6-9
favorite_places = {
    'christy': ['france', 'japan', 'italy'],

    'athena': ['korea', 'japan', 'china'],

    'jaye': ['united kindom', 'netherlands', 'italy'],
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())


# 6-10
favorite_numbers = {
    'christy': ['7','4', '18'],
    'lavande': ['18','26','64'],
    'season': ['18','3'],
    'saturn': ['4','777'],
    'eric': ['8','6','3'],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t" + number.title())


# 6-11
cities = {
    'guangzhou': ['china', '14 million', 'flower city'],

    'paris': ['france', '2 million', 'romantic city'],

    'vienna': ['austria', '1.7 million', 'music city'],
}

for city, infos in cities.items():
    print("\n" + city.title() + ":")
    for info in infos:
        print("\t" + info.title())


# 6-12
aliens = {
    'alien_0': {
        'color': 'green',
        'points': 5,
        'speed': 'slow',
        },

    'alien_1': {
        'color': 'yellow',
        'points': 10,
        'speed': 'medium',
        },

    'alien_2': {
        'color': 'red',
        'points': 15,
        'speed': 'fast',
        },

    }

for alien_name, characters in aliens.items():
    color = characters['color']
    points = characters['points']
    speed = characters['speed']

    print("\nYou killed a " + speed + " " + color + " alien!")
    print("\nYou got" + " " + str(points) + " points!\n")
