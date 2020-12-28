def transform(subject, loop):
    val = 1
    for _ in range(loop):
        val = (val * subject) % 20201227
    return val


def find_loop(key, subject):
    val = 1
    loop = 0
    while True:
        if val == key:
            return loop
        val = (val * subject) % 20201227
        loop += 1


# input
with open('input.txt') as f:
    public = [int(x) for x in f.readlines()]

# part 1
loop = []
for key in public:
    loop.append(find_loop(key, 7))
ans1 = transform(public[0], loop[1])
assert ans1 == transform(public[1], loop[0])

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(':)'))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
