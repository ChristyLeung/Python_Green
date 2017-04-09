# Try 4-13
buffets = ('cheese cake', 'sushi', 'dimsum', 'spaghetti', 'beef steak')
for buffet in buffets:
    print(buffet)

buffets = ('cheese cake', 'sushi', 'dimsum', 'spaghetti', 'beef steak')
buffets[3] = 'pizza'

buffets = ('cheese cake', 'sushi', 'dimsum', 'spaghetti', 'beef steak')
print("Original buffets:")
for buffet in buffets:
    print(buffet)

buffets = ('cheese cake', 'sashimi', 'dimsum', 'pizza', 'beef steak')
print("\nModified buffets:")
for buffet in buffets:
    print(buffet)
