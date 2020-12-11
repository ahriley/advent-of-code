from collections import Counter

# input
with open('input.txt') as f:
    lines = f.readlines()
data = [int(line) for line in lines]
data.append(0)
data.append(max(data) + 3)

# part 1
data = sorted(data)
diff = [data[ii+1] - data[ii] for ii in range(len(data)-1)]
c = Counter(diff)
ans1 = c[1] * c[3]

# part 2
paths = [0] * len(data)
paths[-1] = 1
for i in range(len(data), -1, -1):
    for j in range(i+1, i+4):
        if j < len(data) and data[j] - 3 <= data[i]:
            paths[i] += paths[j]
ans2 = paths[0]

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
