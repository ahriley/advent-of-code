with open('input.txt') as f:
    lines = f.readlines()

# part 1
ans1 = 0
for i in range(len(lines)):
    line = lines[i].strip('\n')

    if line[(3*i) % len(line)] == '#':
        ans1 += 1

# part 2
rights = [1, 3, 5, 7, 1]
downs = [1, 1, 1, 1, 2]
ans2 = 1
for dx, dy in zip(rights, downs):
    row = 0
    count = 0
    numtrees = 0
    while row < len(lines):
        line = lines[row].strip('\n')

        if line[(dx*count) % len(line)] == '#':
            numtrees += 1

        row += dy
        count += 1
    ans2 *= numtrees

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer))
