from math import prod

# input
with open('input.txt') as f:
    lines = f.readlines()
earliest = int(lines[0])
times = [(int(x), -i) for i, x in enumerate(lines[1].split(',')) if x != 'x']

# part 1
bustimes = [bus * ((earliest // bus) + 1) for bus, _ in times]
mintime = min(bustimes)
ans1 = (mintime - earliest) * times[bustimes.index(mintime)][0]

# part 2
# useful link: https://en.wikipedia.org/wiki/Chinese_remainder_theorem
N = prod(time[0] for time in times)
time = 0
for busnum, delta in times:
    Ni = N // busnum
    xi = Ni ** (busnum - 2) % busnum
    time += delta * Ni * xi
ans2 = time % N

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
