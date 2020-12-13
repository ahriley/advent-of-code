# input
with open('input.txt') as f:
    lines = f.readlines()

changes = {'N': [0, 1], 'S': [0, -1], 'W': [-1, 0], 'E': [1, 0]}


# part 1
def change_direction(current, action, value):
    directions = ['N', 'E', 'S', 'W']
    assert value % 90 == 0
    di = int(value / 90)
    if action == 'L':
        di *= -1
    i_old = directions.index(current)
    i_new = (i_old + di) % 4
    return directions[i_new]


pos = [0, 0]
face = 'E'
for line in lines:
    cmd = line[0]
    val = int(line[1:])
    if cmd in changes:
        pos[0] += changes[cmd][0] * val
        pos[1] += changes[cmd][1] * val
    elif cmd == 'F':
        pos[0] += changes[face][0] * val
        pos[1] += changes[face][1] * val
    elif cmd in ['L', 'R']:
        face = change_direction(face, cmd, val)
ans1 = abs(pos[0]) + abs(pos[1])

# part 2
x, y = 0, 0
wx, wy = 10, 1
sin = {0: 0, 90: 1, 180: 0, 270: -1, 360: 0}
for line in lines:
    cmd = line[0]
    val = int(line[1:])
    if cmd in ['L', 'R']:
        if cmd == 'R':
            val = (-val) % 360
        s, c = sin[val], sin[val + 90]
        wx, wy = wx * c - wy * s, wx * s + wy * c
    elif cmd == 'F':
        x, y = x + wx * val, y + wy * val
    elif cmd in changes:
        dx, dy = changes[cmd]
        wx, wy = wx + dx * val, wy + dy * val
ans2 = abs(x) + abs(y)

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
