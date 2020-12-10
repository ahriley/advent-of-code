# input
with open('input.txt') as f:
    lines = f.readlines()

data = []
for line in lines:
    data.append(int(line))


def findsum(preamble, val):
    for ii in range(len(preamble)):
        for jj in range(ii+1, len(preamble)):
            if preamble[ii] + preamble[jj] == val:
                return True
    return False


# part 1
length = 25
for ii in range(length, len(data)):
    preamble = data[ii-length:ii]
    if not findsum(preamble, data[ii]):
        ans1 = data[ii]
        break


def runsum(allowed, start, val):
    for ii in range(start+1, len(allowed)):
        run = sum(data[start:ii])
        if run == val:
            return True, ii
        elif run > val:
            return False, -1
    return False, -1


# part 2
allowed = data[:data.index(ans1)]
for ii in range(len(allowed)):
    result = runsum(allowed, ii, ans1)
    if result[0]:
        vals = data[ii:result[1]]
        ans2 = min(vals) + max(vals)
        break

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
