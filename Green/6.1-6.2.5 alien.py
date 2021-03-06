# 6.1
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])


# 6.2
# 6.2.1
alien_0 = {'color': 'green'}
print(alien_0['color'])


alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print("\nYou just earned " + str(new_points) + " points!\n")


# 6.2.2
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


# 6.2.3
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# 6.2.4
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")


alien_0 = {'x_position': 0, 'color': 'green', 'y_position': 25, 'speed': 'medium'}
print("\nOriginal x-postion: " + str(alien_0['x_position']))

# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的速度一定很快
    x_increment = 3

# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("\nNew x-postion: " + str(alien_0['x_position']))


alien_0 = {'x_position': 0, 'color': 'green', 'y_position': 25, 'speed': 'fast'}
print("\nOriginal x-postion: " + str(alien_0['x_position']))

# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3
else:
    # 这个外星人的速度一定非常快
    x_increment = 4

# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("\nNew x-postion: " + str(alien_0['x_position']))


# 6.2.5
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
