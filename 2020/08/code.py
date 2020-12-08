# input
with open('input.txt') as f:
    lines = f.readlines()


def process_step(instruction, change=False):
    op, arg = instruction.strip().split()
    assert op in ['acc', 'jmp', 'nop']

    if change:
        if op == 'jmp':
            op = 'nop'
        elif op == 'nop':
            op = 'jmp'

    dacc = int(arg) if op == 'acc' else 0
    dline = int(arg) if op == 'jmp' else 1

    return dacc, dline


# part 1
ii = 0
ans1 = 0
used = []
while ii not in used:
    dacc, dline = process_step(lines[ii])

    used.append(ii)
    ans1 += dacc
    ii += dline

# part 2
change_ii = -1
search = True
while search:
    change_ii += 1

    # don't need to test lines that accumulate
    if lines[change_ii][:3] == 'acc':
        continue

    # essentially part 1
    ii = 0
    ans2 = 0
    used = []
    while ii not in used:
        # break out if the end of the list arrives
        if ii == len(lines):
            search = False
            break

        # change line when we get to it
        dacc, dline = process_step(lines[ii], change=ii == change_ii)

        used.append(ii)
        ans2 += dacc
        ii += dline

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
