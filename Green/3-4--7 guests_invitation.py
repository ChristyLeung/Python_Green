# Try 3-4
guests_invitation = ['athena', 'jaye', 'season', 'sheeta']
message_0 = "Would you like to have dinner with me?"
print(guests_invitation[0].title() + ": " + message_0)
print(guests_invitation[1].title() + ": " + message_0)
print(guests_invitation[2].title() + ": " + message_0)
print(guests_invitation[3].title() + ": " + message_0)


# Try 3-5
cannot_come = guests_invitation[2]
message_1 = " is not able to come."
print(cannot_come.title() + message_1)

guests_invitation[2] = 'ines'
print(guests_invitation[2].title() + ": " + message_0)

message_2 = "I've found a bigger table."
print(message_2)

# Try 3-6
guests_invitation = ['athena', 'jaye', 'season', 'sheeta']
guests_invitation.insert(0, 'camie')
print(guests_invitation)
guests_invitation.insert(2, 'mickey')
print(guests_invitation)
guests_invitation.append('miriam')
print(guests_invitation)

print(guests_invitation[0].title() + ": " + message_2 + message_0)
print(guests_invitation[2].title() + ": " + message_2 + message_0)
print(guests_invitation[6].title() + ": " + message_2 + message_0)

print("I'm afraid I could only invite two people this time.")


# Try 3-7
print(guests_invitation)
message_3 = "I'm sorry to inform you that I couldn't invite to have dinner with me this time."

print(guests_invitation.pop(0).title() + ": " + message_3)
print(guests_invitation)

print(guests_invitation.pop(1).title() + ": " + message_3)
print(guests_invitation)

print(guests_invitation.pop(2).title() + ": " + message_3)
print(guests_invitation)

print(guests_invitation.pop(3).title() + ": " + message_3)
print(guests_invitation)

print(guests_invitation.pop(0).title() + ": " + message_3)
print(guests_invitation)

message_4 = "You're always welcomed to have dinner with me!"
print(guests_invitation[0].title() + ": " + message_4)
print(guests_invitation[1].title() + ": " + message_4)

print(guests_invitation)

del guests_invitation[0]
del guests_invitation[0]
print(guests_invitation)
