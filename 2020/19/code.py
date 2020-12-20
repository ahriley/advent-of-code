import re


# recursively convert rules to regex. maxdepth = 15 (for part 2)
def convert_to_regex(rules, key, depth=0):
    if depth > 15:
        return ''

    if rules[key] in ('a', 'b'):
        return rules[key]

    resolved = []
    for branches in rules[key].split('|'):
        branch_answer = ''
        for branch_num in branches.split():
            branch_re = convert_to_regex(rules, branch_num, depth+1)
            branch_answer += branch_re
        resolved.append(branch_answer)

    return '(' + '|'.join(resolved) + ')'


# number of valid messages given the rules
def num_valid(rules, messages):
    regex = re.compile(convert_to_regex(rules, '0'))
    valid = [bool(regex.fullmatch(message)) for message in messages]
    return sum(valid)


# input
with open('input.txt') as f:
    blocks = f.read().strip().split('\n\n')

# parse rules
rules = {}
for line in blocks[0].split('\n'):
    if line[0].isdigit():
        items = line.split(': ')
        val = items[1].strip()
        rules[items[0]] = val.strip('"') if '"' in val else val
messages = blocks[1].split('\n')

# part 1
ans1 = num_valid(rules, messages)

# part 2
rules['8'] = '42 | 42 8'
rules['11'] = '42 31 | 42 11 31'
ans2 = num_valid(rules, messages)

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
