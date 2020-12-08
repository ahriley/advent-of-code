# input
with open('input.txt') as f:
    lines = f.readlines()

# ingest rules as dictionary
# key: outside bag, val: (how many, inside color)
rules = {}
for line in lines:
    items = line.split()

    key = items[0] + items[1]
    assert items[2:4] == ['bags', 'contain']

    if items[4:] == ['no', 'other', 'bags.']:
        val = None
    else:
        colors, numbers = [], []
        assert len(items[4:]) % 4 == 0
        for i in range(int(len(items[4:])/4)):
            colors.append(items[4*i+5]+items[4*i+6])
            numbers.append(int(items[4*i+4]))
        val = [colors, numbers]
    rules[key] = val


# recursive function for stepping through bag rules
def containstarget(key, target):
    val = rules[key]
    if val is None:
        return False
    elif target in val[0]:
        return True

    return any([containstarget(color, target) for color in val[0]])


# recursive function for counting bags within a given color
def countbags(key):
    if rules[key] is None:
        return 1

    val = rules[key]
    return sum([num*countbags(c) for c, num in zip(val[0], val[1])]) + 1


# part 1
ans1 = 0
for color in rules.keys():
    ans1 += containstarget(color, 'shinygold')

# part 2
ans2 = countbags('shinygold') - 1

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
