import numpy as np

# input
with open('input.txt') as f:
    lines = f.readlines()

# part 1
code = {'F': 0, 'B': 1, 'L': 0, 'R': 1}
vals = [64, 32, 16, 8, 4, 2, 1, 4, 2, 1]
seats = []
for line in lines:
    seat = 0
    for char, val in zip(line, vals):
        scale = 8 if char in 'FB' else 1
        seat += scale * code[char] * val
    seats.append(seat)
seats = np.array(seats)
ans1 = seats.max()

# part 2
seats = np.sort(seats)
diff = seats[1:] - seats[:-1]
ans2 = seats[1:][diff == 2][0] - 1

# output
answer = []
answer.append('Part 1: {}'.format(ans1))
answer.append('Part 2: {}'.format(ans2))
with open('solution.txt', 'w') as f:
    f.writelines('\n'.join(answer)+'\n')
