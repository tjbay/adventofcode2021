filename = "input.txt"

with open(filename, "rt") as f:
    data = f.read().strip().split('\n')

# part 1

moves = {'forward': 0, 'up': 0, 'down': 0}

for item in data:
    command, step = item.split()
    if command in moves:
        moves[command] += int(step)

horizontal_pos = moves['forward']
depth = moves['down'] - moves['up']
# print(horizontal_pos*depth)

# part 2
"""
down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
It increases your horizontal position by X units.
It increases your depth by your aim multiplied by X.
"""

state = {'aim': 0, 'depth': 0, 'horizontal': 0}

for item in data:
    command, value = item.split()
    value = int(value)
    if command == 'down':
        state['aim'] += value
    elif command == 'up':
        state['aim'] -= value
    elif command == 'forward':
        state['horizontal'] += value
        state['depth'] += state['aim'] * value

print(state['depth'] * state['horizontal'])



