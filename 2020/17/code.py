# input
with open('input.txt') as f:
    lines = f.readlines()


def neighbors_3d(cube):
    x, y, z = cube

    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if i == j == k == 0:
                    continue
                neighbors.append((x+i, y+j, z+k))
    return neighbors


def neighbors_4d(cube):
    x, y, z, w = cube

    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for h in range(-1, 2):
                    if i == j == k == h == 0:
                        continue
                    neighbors.append((x+i, y+j, z+k, w+h))
    return neighbors


def sumneighbors(grid, cube, neighborfunc):
    return len([key for key in neighborfunc(cube) if grid.get(key) == '#'])


def possible_changes(grid, neighborfunc):
    active = []
    for key in grid:
        if grid.get(key) == '#':
            active += neighborfunc(key)
            active.append(key)
    return list(set(active))


def play_rounds(grid, n, neighborfunc):
    for i in range(n):
        nextgrid = {}
        for key in possible_changes(grid, neighborfunc):
            nearsum = sumneighbors(grid, key, neighborfunc)
            if grid.get(key) == '#':
                nextgrid[key] = '#' if nearsum in [2, 3] else '.'
            else:
                nextgrid[key] = '#' if nearsum == 3 else '.'
        grid = nextgrid
    return grid


# part 1
start_3d = {}
for i, line in enumerate(lines):
    items = line.strip()
    for j, state in enumerate(items):
        start_3d[(i, j, 0)] = state
final = play_rounds(start_3d, 6, neighbors_3d)
ans1 = len([key for key in final if final.get(key) == '#'])

# part 2
start_4d = {}
for key in start_3d:
    newkey = (key[0], key[1], key[2], 0)
    start_4d[newkey] = start_3d[key]
final = play_rounds(start_4d, 6, neighbors_4d)
ans2 = len([key for key in final if final.get(key) == '#'])

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
