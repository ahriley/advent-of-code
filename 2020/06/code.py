from collections import Counter

# input
with open('input.txt') as f:
    lines = f.readlines()

# part 1
yes = ''
ans1 = 0
for line in lines:
    if line == '\n':
        ans1 += len(yes)
        yes = ''
        continue

    for char in line.strip('\n'):
        if char not in yes:
            yes += char
ans1 += len(yes)

# part 2
ans2 = 0
numpeople = 0
groupstring = ''
for line in lines:
    if line == '\n':
        count = Counter(groupstring)
        ans2 += sum([count[key] == numpeople for key in count.keys()])

        groupstring = ''
        numpeople = 0
        continue

    groupstring += line.strip('\n')
    numpeople += 1
count = Counter(groupstring)
ans2 += sum([count[key] == numpeople for key in count.keys()])

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
