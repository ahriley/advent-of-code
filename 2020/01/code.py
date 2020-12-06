import numpy as np

data = np.loadtxt('input.txt')
answer = []

# part 1
for x in data:
    y = data + x
    if (y == 2020).any():
        ans1 = int((2020 - x) * x)
        break
answer.append('Part 1: '+str(ans1))

# part 2
for i in range(len(data)):
    for j in range(i, len(data)):
        z = data + data[i] + data[j]
        if (z == 2020).any():
            ans2 = int((2020 - data[i] - data[j]) * data[i] * data[j])
            break
answer.append('Part 2: '+str(ans2))

with open('solution.txt', 'w') as f:
    f.write("\n".join(answer))
