with open('input_day2.txt') as f:
    input = f.readlines()
    input = [i.strip().split() for i in input]

x = 0
aim = 0
z = 0

for i in input:
    direction  = i[0]
    value = int(i[1])
    if direction == 'forward':
        x+=value
    elif direction == 'up':
        z+=value
    elif direction == 'down':
        z-=value

print('Part1: ',x*z)
x = 0
aim = 0
z = 0

for i in input:
    direction  = i[0]
    value = int(i[1])
    if direction == 'forward':
        x+=value
        z += aim*value
    elif direction == 'up':
        aim+=value
    elif direction == 'down':
        aim-=value

print('Part2: ', x*z)
