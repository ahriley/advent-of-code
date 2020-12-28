# using cube coordinates: https://www.redblobgames.com/grids/hexagons/
def update(tile, command):
    x, y, z = tile
    if command == 'w':
        x -= 1
        y += 1
    elif command == 'e':
        x += 1
        y -= 1
    elif command == 'nw':
        y += 1
        z -= 1
    elif command == 'se':
        y -= 1
        z += 1
    elif command == 'ne':
        x += 1
        z -= 1
    elif command == 'sw':
        x -= 1
        z += 1
    assert x + y + z == 0
    return [x, y, z]


def neighbors(tile):
    directions = ['w', 'e', 'nw', 'ne', 'sw', 'se']
    return [update(tile, direction) for direction in directions]


# input
with open('input.txt') as f:
    lines = f.readlines()

# part 1
flipped = []
for line in lines:
    commands = line.replace('w', 'w,').replace('e', 'e,').split(',')[:-1]
    tile = [0, 0, 0]
    for command in commands:
        tile = update(tile, command)
    flipped.remove(tile) if tile in flipped else flipped.append(tile)
ans1 = len(flipped)

# part 2
for _ in range(100):
    possible = []
    for tile in flipped:
        possible += [adj for adj in neighbors(tile) if adj not in possible]
    possible += [tile for tile in flipped if tile not in possible]

    next_flipped = flipped.copy()
    for tile in possible:
        num = len([adj for adj in neighbors(tile) if adj in flipped])
        if tile in flipped:
            if num == 0 or num > 2:
                next_flipped.remove(tile)
        else:
            if num == 2:
                next_flipped.append(tile)

    flipped = next_flipped
ans2 = len(flipped)

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
