# input
with open('input.txt') as f:
    lines = f.readlines()


def play(numbers, turns):
    mem = {val: idx + 1 for idx, val in enumerate(numbers)}
    prev = numbers[-1]
    for turn in range(len(numbers), turns):
        nextnum = 0 if prev not in mem else turn - mem[prev]
        mem[prev] = turn
        prev = nextnum
    return prev


start = [int(num) for num in lines[0].split(',')]
ans1 = play(start, 2020)
ans2 = play(start, 30000000)

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
