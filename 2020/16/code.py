# input
with open('input.txt') as f:
    lines = f.readlines()

# process the input
blocks = [block.strip().split('\n') for block in ''.join(lines).split('\n\n')]
rules = {}
for rule in blocks[0]:
    key, lim = rule.split(': ')
    pairs = [pair.split('-') for pair in lim.split(' or ')]
    limits = [(int(pair[0]), int(pair[1])) for pair in pairs]
    rules[key] = limits
you = [int(n) for n in blocks[1][1].split(',')]
others = [[int(n) for n in ticket.split(',')] for ticket in blocks[2][1:]]

# part 1
ans1 = 0
others_valid = []
for ticket in others:
    ticket_valid = True
    for n in ticket:
        valid = False
        for field in rules:
            valid |= rules[field][0][0] <= n <= rules[field][0][1]
            valid |= rules[field][1][0] <= n <= rules[field][1][1]
        ticket_valid &= valid
        if not valid:
            ans1 += n
            continue
    others_valid.append(ticket_valid)

# part 2
valid = []
for ticket, status in zip(others, others_valid):
    if status:
        valid.append(ticket)
others = valid

# which keys are valid for a particular column
valid_keys = []
for ii in range(len(you)):
    keys = []
    for key in rules:
        valid = True
        for ticket in others:
            test = rules[key][0][0] <= ticket[ii] <= rules[key][0][1]
            test |= rules[key][1][0] <= ticket[ii] <= rules[key][1][1]
            valid &= test
        if valid:
            keys.append(key)
    valid_keys.append(keys)

# sort the valid key lists by their length, then step through and assign
numvalid = [len(li) for li in valid_keys]
valid_keys_sorted = [x for _, x in sorted(zip(numvalid, valid_keys))]
fields = []
for li in valid_keys_sorted:
    for key in li:
        if key not in fields:
            fields.append(key)
            continue

# product of 'departure' values for your ticket
columns = list(range(len(you)))
columns_sorted = [x for _, x in sorted(zip(numvalid, columns))]
ans2 = 1
for field, ii in zip(fields, columns_sorted):
    if field.startswith('departure'):
        ans2 *= you[ii]

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
