# input
with open('input.txt') as f:
    lines = f.readlines()


def resolve_1(expression):
    result = int(expression[0])
    loc = 1
    while loc < len(expression):
        if expression[loc] == '+':
            result += int(expression[loc+1])
            loc += 1
        elif expression[loc] == '*':
            result *= int(expression[loc+1])
            loc += 1
        loc += 1
    return result


def resolve_2(expression):
    temp = []
    loc = 0
    while loc < len(expression):
        if expression[loc] == '+':
            temp[-1] += int(expression[loc+1])
            loc += 1
        elif expression[loc].isdigit():
            temp.append(int(expression[loc]))
        loc += 1

    result = 1
    for num in temp:
        result *= num

    return result


def process(expression, resolvefunc):
    assert expression.count('(') == expression.count(')')
    if '(' in expression:
        new = []
        start = expression.index('(')
        for idx in range(start+1, len(expression)):
            if expression[idx] == ')' and new.count('(') == new.count(')'):
                break
            new.append(expression[idx])
        resolved = [str(process(new, resolvefunc))]
        step = expression[:start] + resolved + expression[start+len(new)+2:]
        return process(step, resolvefunc)
    return resolvefunc(expression)


# parts 1 and 2 executed
lines = [list(line.strip().replace(' ', '')) for line in lines]
ans1 = sum([process(line, resolve_1) for line in lines])
ans2 = sum([process(line, resolve_2) for line in lines])

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
