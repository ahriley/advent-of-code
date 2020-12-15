# input
with open('input.txt') as f:
    lines = f.readlines()


# part 1
def process_line(mask, value):
    output = ['0'] * 36
    binval = bin(value)[2:]

    for ii in range(len(binval)):
        output[len(output)-1-ii] = binval[len(binval)-1-ii]
    for ii in range(len(mask)):
        if mask[ii] != 'X':
            output[ii] = mask[ii]

    return int(''.join(output), 2)


memory = {}
for line in lines:
    items = line.strip().split(' = ')
    if items[0] == 'mask':
        mask = items[1]
    else:
        key = int(items[0].strip('mem[]'))
        inval = int(items[1])
        memory[key] = process_line(mask, inval)
ans1 = sum(memory.values())


# part 2
def decode(mask, value):
    output = ['0'] * 36
    binval = bin(value)[2:]

    for ii in range(len(binval)):
        output[len(output)-1-ii] = binval[len(binval)-1-ii]
    for ii in range(len(mask)):
        if mask[ii] != '0':
            output[ii] = mask[ii]

    return floating(output)


def floating(value):
    if 'X' in value:
        value_0 = value.copy()
        value_1 = value.copy()

        value_0[value.index('X')] = '0'
        value_1[value.index('X')] = '1'

        return floating(value_0) + floating(value_1)
    return [int(''.join(value), 2)]


memory = {}
for line in lines:
    items = line.strip().split(' = ')
    if items[0] == 'mask':
        mask = items[1]
    else:
        inkey = int(items[0].strip('mem[]'))
        val = int(items[1])
        keys = decode(mask, inkey)
        for key in keys:
            memory[key] = val
ans2 = sum(memory.values())

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
