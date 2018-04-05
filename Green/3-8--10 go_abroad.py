# Try 3-8
go_abroad = ['France', 'Japan', 'Italy', 'America', 'Australia']
print(go_abroad)

print(sorted(go_abroad))

print(sorted(go_abroad))
go_abroad.sort(reverse=True)
print(go_abroad)

print(go_abroad)

go_abroad.reverse()
print(go_abroad)

go_abroad.reverse()
print(go_abroad)

go_abroad.sort()
print(go_abroad)

go_abroad.sort(reverse=True)
print(go_abroad)


# Try 3-9
guests_invitation = ['athena', 'jaye', 'season', 'sheeta']
print (len(guests_invitation))


# Try 3-10
languages = ['English', 'Japanese', 'French', 'Italian', 'Spainish', 'Korean']
print(languages)

print(languages[2])

message_0 = 'My favorite language is '
print(message_0 + languages[2] + '.')

languages.append('Chinese')
print(languages)

languages[-1] = 'Arabic'
print(languages)

languages.insert(4, 'Chinese')
print(languages)

del languages[3]
print(languages)

popped_language = languages.pop()
print(languages)
print(popped_language)

languages = ['English', 'Japanese', 'French', 'Italian', 'Spainish', 'Korean']
first_language = languages.pop(3)
print(first_language + " is my first language.")


seventh_language = languages.pop()
print("The seventh language I learn is " + seventh_language + '.')

popular_language = 'Spainish'
print(popular_language)
print(popular_language + " is the second language of the majority of Americans.")
languages.remove(popular_language)
languages.append('Chinese')
print(popular_language)

languages.sort()
print(languages)

languages.sort(reverse=True)
print(languages)

print("\nHere is the most romantic language in the world:")
print(languages[1])

languages.reverse()
print(languages)

languages = ['Chinese', 'English', 'French', 'Japanese']
print (len(languages))
