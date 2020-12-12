# input
with open('input.txt') as f:
    lines = f.readlines()

start = {}
for i in range(len(lines)):
    for j in range(len(lines[i].strip())):
        start[(i, j)] = lines[i][j]


def sumocc(grid, seats):
    occ = 0
    for key in seats:
        if grid.get(key) == '#':
            occ += 1
    return occ


def rounds(start_grid, ntol, func):
    included = {}
    for spot in start_grid:
        included[spot] = func(start_grid, spot)

    grids = [start_grid]
    change = True
    while change:
        temp = {}
        change = False

        for seat in grids[-1]:
            neighbors = sumocc(grids[-1], included[seat])
            if grids[-1].get(seat) == 'L' and neighbors == 0:
                temp[seat] = '#'
                change = True
            elif grids[-1].get(seat) == '#' and neighbors >= ntol:
                temp[seat] = 'L'
                change = True
            else:
                temp[seat] = grids[-1].get(seat)

        if change:
            grids.append(temp)

    return grids


# part 1
def close(grid, spot):
    x, y = spot
    close = [(x-1, y-1), (x-1, y), (x-1, y+1)]
    close.extend([(x, y-1), (x, y+1)])
    close.extend([(x+1, y-1), (x+1, y), (x+1, y+1)])
    return close


grids = rounds(start, 4, close)
ans1 = sumocc(grids[-1], grids[-1].keys())


# part 2
def visible(grid, spot):
    x, y = spot
    visible = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            test = (x+dx, y+dy)
            while grid.get(test) is not None:
                if grid.get(test) != '.':
                    visible.append(test)
                    break
                test = (test[0]+dx, test[1]+dy)

    return visible


grids = rounds(start, 5, visible)
ans2 = sumocc(grids[-1], grids[-1].keys())

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
