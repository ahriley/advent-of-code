import numpy as np

# read in file
with open('input.txt') as f:
    lines = f.readlines()

# process file
lows, highs, vals, passwords = [], [], [], []
for line in lines:
    items = line.split()
    limits = items[0].split('-')
    lows.append(int(limits[0]))
    highs.append(int(limits[1]))
    vals.append(items[1][0])
    passwords.append(items[2])
lows = np.array(lows)
highs = np.array(highs)

# part 1
counts = []
for val, password in zip(vals, passwords):
    counts.append(password.count(val))
counts = np.array(counts)
valid = (counts >= lows) & (counts <= highs)

# part 2
sumvalid = 0
for low, high, val, password in zip(lows, highs, vals, passwords):
    useful = [password[low-1], password[high-1]]
    if useful.count(val) == 1:
        sumvalid += 1

# output
answer = []
answer.append('Part 1: {}'.format(np.sum(valid)))
answer.append('Part 2: {}'.format(sumvalid))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer))
