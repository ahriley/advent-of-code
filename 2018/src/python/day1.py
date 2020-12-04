import numpy as np

with open('data/day1.txt') as f:
    lines = f.read()
input = lines.split('\n')
changes = np.array([int(delta) for delta in input[:-1]])
progress = np.cumsum(changes)

# part 1: end number
print(progress[-1])

# part 2: first number reached twice
firstround = len(np.unique(progress)) != len(progress)
unique = set([]); found = False
current = progress; currentset = set(progress);

while not found:
    if unique.intersection(currentset) != set() or firstround:
        for num in current:
            numset = set([num])
            if unique.intersection(numset) != set():
                result = num
                found = True
                break
            unique = unique.union(numset)
    unique = unique.union(currentset)
    current = progress+current[-1]
    currentset = set(current)
print(result)
